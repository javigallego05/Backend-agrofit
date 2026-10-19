import time
import usuarios.conexion as conexion

class MenuEntrenador:
    def __init__(self, nombre_usuario):
        self.nombre_usuario = nombre_usuario

    def iniciar(self):
        while True:
            print("\n" + "="*55)
            print(f" BIENVENIDO ENTRENADOR: {self.nombre_usuario.upper()} ")
            print("="*55)
            print("1. Crear y asignar rutina a aprendiz")
            print("2. Inventario y Mantenimiento de Máquinas")
            print("3. Salir")
            print("="*55)

            opcion = input("Elige una opción (1-3): ")

            if opcion == "1":
                self.asignar_rutina()
            elif opcion == "2":
                self.menu_inventario()
            elif opcion == "3":
                print("\nCerrando sesión del portal entrenador. ¡Hasta pronto!")
                break
            else:
                print("\nOpción no válida. Intenta de nuevo.")

    def asignar_rutina(self):
        print("\n" + "-"*40)
        print(" ASIGNAR RUTINA A USUARIO ".center(40))
        print("-" * 40)

        documento_usuario = input("Ingresa el documento del aprendiz o funcionario: ")
        nombre_rutina = input("Ingresa el nombre de la rutina : ")
        print("\nProcesando...")
        time.sleep(1)

        try:
            connect = conexion.connect()
            database = connect[0]
            cursor = connect[1]

            sql_buscar = "SELECT id_usuario FROM usuarios WHERE numero_documento = %s"
            cursor.execute(sql_buscar, (documento_usuario,))
            usuario_encontrado = cursor.fetchone()

            if usuario_encontrado:
                id_usuario = usuario_encontrado[0]
                id_rutina_por_defecto = 1

                sql_insertar = "INSERT INTO asignacion_rutinas (nombre_asignacion, id_rutina, id_usuario) VALUES (%s, %s, %s)"
                cursor.execute(sql_insertar, (nombre_rutina, id_rutina_por_defecto, id_usuario))
                database.commit()

                print(f"¡Éxito! La rutina '{nombre_rutina}' ha sido asignada al aprendiz.")
            else:
                print("Error: No se encontró ningún usuario registrado con ese número de documento.")
                
        except Exception as e:
            print(f"Error al conectar con la base de datos: {e}")
        
        time.sleep(1.5)

    # =========================================================
    # MÓDULO DE INVENTARIO Y MANTENIMIENTO DE MÁQUINAS
    # =========================================================

    def menu_inventario(self):
        while True:
            print("\n" + "="*55)
            print(" INVENTARIO Y MANTENIMIENTO DE MÁQUINAS ".center(55))
            print("="*55)
            print("1. Ver Inventario y Métricas")
            print("2. Registrar Nuevo Equipo")
            print("3. Reportar Novedad / Cambiar Estado")
            print("4. Volver al menú principal")
            print("="*55)

            opcion = input("Selecciona una opción (1-4): ")

            if opcion == "1":
                self.ver_inventario()
            elif opcion == "2":
                self.registrar_equipo()
            elif opcion == "3":
                self.reportar_novedad()
            elif opcion == "4":
                break
            else:
                print("\nOpción no válida.")

    def ver_inventario(self):
        print("\n" + "-"*60)
        print(" RESUMEN Y ESTADÍSTICAS DEL INVENTARIO ".center(60))
        print("-" * 60)

        try:
            connect = conexion.connect()
            cursor = connect[1]

            # Consulta para conteo de estados (KPIs del prototipo HTML)
            cursor.execute("SELECT COUNT(*) FROM maquinas")
            total = cursor.fetchone()[0]

            cursor.execute("SELECT COUNT(*) FROM maquinas WHERE estado = 'Operativo'")
            operativos = cursor.fetchone()[0]

            cursor.execute("SELECT COUNT(*) FROM maquinas WHERE estado = 'Mantenimiento'")
            mantenimiento = cursor.fetchone()[0]

            cursor.execute("SELECT COUNT(*) FROM maquinas WHERE estado = 'Fuera de Servicio'")
            fuera_servicio = cursor.fetchone()[0]

            print(f" TOTAL EQUIPOS: {total}  |  OPERATIVOS: {operativos}  |  EN MANTENIMIENTO: {mantenimiento}  |  FUERA DE SERVICIO: {fuera_servicio}")
            print("-" * 60)

            # Consulta de la lista detallada de equipos
            cursor.execute("SELECT placa, nombre_maquina, marca, ubicacion, estado, observaciones FROM maquinas")
            maquinas = cursor.fetchall()

            if maquinas:
                print("\nLISTADO DE EQUIPOS REGISTRADOS:\n")
                for m in maquinas:
                    print(f" Placa: {m[0]} | Estado: [{m[4]}]")
                    print(f" Nombre: {m[1]} ({m[2]})")
                    print(f" Ubicación: {m[3]}")
                    print(f" Nota: {m[5] if m[5] else 'Sin novedades'}")
                    print("-" * 40)
            else:
                print("\nNo hay máquinas registradas en la base de datos.")

        except Exception as e:
            print(f"Error al consultar el inventario: {e}")

        input("\nPresiona Enter para continuar...")

    def registrar_equipo(self):
        print("\n" + "-"*50)
        print(" REGISTRAR NUEVO EQUIPO ".center(50))
        print("-" * 50)

        placa = input("Placa/Código del equipo (Ej: AG-EQ-004): ")
        nombre = input("Nombre de la máquina: ")
        marca = input("Marca / Categoría: ")
        ubicacion = input("Ubicación en el gym (Ej: Zona Cardio): ")

        try:
            connect = conexion.connect()
            db = connect[0]
            cursor = connect[1]

            sql = """
                INSERT INTO maquinas (placa, nombre_maquina, marca, ubicacion, estado, observaciones)
                VALUES (%s, %s, %s, %s, 'Operativo', 'Equipo nuevo en servicio')
            """
            cursor.execute(sql, (placa, nombre, marca, ubicacion))
            db.commit()

            print(f"\n¡Éxito! El equipo '{nombre}' [{placa}] ha sido registrado correctamente.")

        except Exception as e:
            print(f"Error al registrar la máquina: {e}")

        time.sleep(1.5)

    def reportar_novedad(self):
        print("\n" + "-"*50)
        print(" REPORTAR NOVEDAD / CAMBIAR ESTADO ".center(50))
        print("-" * 50)

        placa = input("Ingresa la placa de la máquina: ")

        print("\nSelecciona el nuevo estado:")
        print("1. Operativo")
        print("2. Mantenimiento")
        print("3. Fuera de Servicio")
        
        op_estado = input("Opción (1-3): ")
        estados = {"1": "Operativo", "2": "Mantenimiento", "3": "Fuera de Servicio"}
        nuevo_estado = estados.get(op_estado, "Operativo")

        novedad = input("Describe la novedad/observación técnica: ")

        try:
            connect = conexion.connect()
            db = connect[0]
            cursor = connect[1]

            sql = "UPDATE maquinas SET estado = %s, observaciones = %s WHERE placa = %s"
            cursor.execute(sql, (nuevo_estado, novedad, placa))
            db.commit()

            if cursor.rowcount > 0:
                print(f"\n¡Novedad actualizada correctamente para el equipo {placa}!")
            else:
                print(f"\nNo se encontró ninguna máquina con la placa '{placa}'.")

        except Exception as e:
            print(f"Error al actualizar la novedad: {e}")

        time.sleep(1.5)