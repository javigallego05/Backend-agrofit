import usuarios.conexion as conexion
import usuarios.usuario as usuario
from aprendiz.inicio_aprendiz import MenuAprendiz
from entrenador.inicio_entrenador import MenuEntrenador
from administrador import inicio_administrador
from funcionario import inicio_funcionario
import random
import hashlib

class Acciones:
    # registro usuario
    def registro(self):
        print("\n--- REGISTRO EN AGROFIT ---")
        nombre = input("¿Cuál es tu nombre?: ")
        apellidos = input("¿Cuáles son tus apellidos?: ")
        correo = input("Introduce tu correo electrónico: ")
        contrasena = input("Introduce tu contraseña: ")

        print("Tipos de documento disponibles:")
        print("1. Cédula de Ciudadanía")
        print("2. Tarjeta de Identidad")
        id_tipo_documento = input("Selecciona el tipo de documento (1 o 2) [1]: ")
        if not id_tipo_documento:
            id_tipo_documento = 1

        numero_documento = input("Introduce tu número de documento: ")
        direccion = input("Introduce tu direccion: ")
        telefono = input("Introduce tu numero de telefono: ")
        edad = input("Introduce tu edad: ")
        altura = input("Introduce tu altura: ")
        peso = input("Introduce tu peso: ")

        print("\nRoles disponibles:")
        print("1. Administrador")
        print("2. Funcionarios")
        print("3. Instructor")
        print("4. Aprendices")

        id_rol = input("Selecciona el rol (1-4): ").strip()

        # Validación simple
        if id_rol not in ["1", "2", "3", "4"]:
            print("Rol no válido. Se asignará 'Aprendices' por defecto.")
            id_rol = "4"

        # Instancia la clase Usuario con los datos capturados
        usuario_obj = usuario.Usuario(
            nombre_usuario=nombre,
            apellido_usuario=apellidos,
            correo=correo,
            contrasena=contrasena,
            id_tipo_documento=id_tipo_documento,
            numero_documento=numero_documento,
            direccion=direccion,
            telefono=telefono,
            edad=edad,
            altura=altura,
            peso=peso,
            id_rol=id_rol
        )
        # Ejecuta la inserción en la BD
        registro = usuario_obj.registrar()

        if registro[0] >= 1:
            print(f"\n¡Perfecto {registro[1].nombre_usuario}! Te has registrado correctamente.")
        else:
            print("\nError: No se ha podido completar el registro (comprueba si el documento o correo ya existen).")

    # inicio usuario
    def login(self):
        print("\n--- INICIO DE SESIÓN EN AGROFIT ---")
        print("Tipos de documento disponibles:")
        print("1. Cédula de Ciudadanía")
        print("2. Tarjeta de Identidad")

        id_tipo = input("Selecciona el tipo de documento (1 o 2) [1]: ") or "1"
        numero_documento = input("Introduce tu número de documento: ")
        contrasena = input("Introduce tu contraseña: ")

        # Conectar a la base de datos (usando tu función real)
        connect = conexion.connect()
        database = connect[0]
        cursor = connect[1]

        # Consulta para buscar el usuario
        query = """
            SELECT nombre_usuario, apellido_usuario, correo, contrasena,
                id_tipo_documento, numero_documento, direccion, telefono,
                edad, altura, peso, id_rol, estado
            FROM usuarios
            WHERE numero_documento = %s AND contrasena = %s AND id_tipo_documento = %s
        """
        cursor.execute(query, (numero_documento, contrasena, id_tipo))
        resultado = cursor.fetchone()

        if resultado:
            # Crear el objeto Usuario con el orden EXACTO de tu __init__
            usuario_obj = usuario.Usuario(
                nombre_usuario=resultado[0],
                apellido_usuario=resultado[1],
                correo=resultado[2],
                contrasena=resultado[3],
                id_tipo_documento=resultado[4],
                numero_documento=resultado[5],
                direccion=resultado[6],
                telefono=resultado[7],
                edad=resultado[8],
                altura=resultado[9],
                peso=resultado[10],
                id_rol=resultado[11],
                estado=resultado[12]
            )
            
        # --- VALIDACIÓN DE ROLES PARA LANZAR MENÚS ---
        rol_seguro = str(usuario_obj.id_rol).strip().lower()

      # 1. Si es Administrador
        if rol_seguro == "administrador" or rol_seguro == "1":
            menu_admin = inicio_administrador.MenuAdministrador(usuario_obj.nombre_usuario, usuario_obj.numero_documento)
            menu_admin.iniciar()

        # 2. Si es Funcionario (Sandra entró con este número)
        elif rol_seguro == "funcionario" or rol_seguro == "funcionarios" or rol_seguro == "2":
            # Usamos el módulo inicio_funcionario que debes tener importado arriba
            menu_func = inicio_funcionario.MenuFuncionario(usuario_obj.nombre_usuario, usuario_obj.numero_documento)
            menu_func.iniciar()

        # 3. Si es Instructor / Entrenador
        elif rol_seguro == "instructor" or rol_seguro == "entrenador" or rol_seguro == "3":
            menu_entrenador = MenuEntrenador(usuario_obj.nombre_usuario)
            menu_entrenador.iniciar()

        # 4. Si es Aprendiz
        elif rol_seguro == "aprendiz" or rol_seguro == "aprendices" or rol_seguro == "4":
            # Tus variables previas para el aprendiz
            dias_completados = 2
            rutina_actual = ""
            menu = MenuAprendiz(usuario_obj.nombre_usuario, usuario_obj.numero_documento, dias_completados)
            menu.iniciar()

        # 5. Si no coincide con ninguno
        else:
            print(f"\n[ERROR DE ROL] El sistema detectó el rol: '{rol_seguro}' y no tiene un menú asignado.")
        # ---------------------------------------------
        return usuario_obj

    # recuperacion de contraseña    
    def recovery(self):
        print("\n--- RECUPERACIÓN DE CONTRASEÑA EN AGROFIT ---")
        
        correo = input("Introduce tu correo electrónico registrado: ").strip()

        # Conectar
        connect = conexion.connect()
        database = connect[0]
        cursor = connect[1]

        # Verificar si el correo existe
        cursor.execute("SELECT nombre_usuario FROM usuarios WHERE correo = %s", (correo,))
        resultado = cursor.fetchone()

        if not resultado:
            print("\nNo existe ningún usuario con ese correo.")
            return

        # Generar código
        codigo_generado = str(random.randint(100000, 999999))
        print(f"\n[Simulación] Código enviado a {correo}: {codigo_generado}")

        codigo_ingresado = input("\nIntroduce el código de 6 dígitos: ").strip()

        if codigo_ingresado != codigo_generado:
            print("\nCódigo incorrecto.")
            return

        # Pedir nueva contraseña
        print("\nCódigo correcto.")
        nueva_contrasena = input("Nueva contraseña: ")
        confirmar = input("Confirma la nueva contraseña: ")

        if nueva_contrasena != confirmar:
            print("\nLas contraseñas no coinciden.")
            return

        # Encriptar (igual que en registrar e identificar)
        cifrado = hashlib.sha256()
        cifrado.update(nueva_contrasena.encode('utf-8'))
        contrasena_encriptada = cifrado.hexdigest()

        # Actualizar
        cursor.execute(
            "UPDATE usuarios SET contrasena = %s WHERE correo = %s",
            (contrasena_encriptada, correo)
        )
        database.commit()

        print("\n¡Contraseña actualizada correctamente! Ya puedes iniciar sesión con la nueva.")
        print(f"Filas afectadas: {cursor.rowcount}")

