
class MenuAdministrador:
    def __init__(self, nombre_usuario, documento):
        self.nombre_usuario = nombre_usuario
        self.documento = documento

    def iniciar(self):
        while True:
            print("\n==================================================")
            print("      PORTAL ADMINISTRADOR - AGROFIT SENA         ")
            print("==================================================")
            print(f"Bienvenido/a, {self.nombre_usuario}\n")
            
            print("1. Inicio & Control")
            print("2. Usuarios & Entrenadores (Gestión de roles)")
            print("3. Fichas SENA")
            print("4. Inventario de Máquinas (Ver equipos)")
            print("5. Cerrar Sesión")
            
            opcion = input("\nSelecciona una opción: ").strip()

            if opcion == "1":
                print("\nMostrando métricas generales de inicio...")
            elif opcion == "2":
                self.gestionar_usuarios()
            elif opcion == "3":
                print("\nMódulo de Fichas SENA en construcción...")
            elif opcion == "4":
                self.ver_maquinas()
            elif opcion == "5":
                print("\nCerrando sesión del portal administrador. ¡Hasta pronto!")
                break
            else:
                print("\n[ERROR] Opción no válida. Intenta de nuevo.")

    def gestionar_usuarios(self):
        while True:
            print("\n--- GESTIÓN INTEGRAL DE USUARIOS Y ENTRENADORES ---")
            print("1. Ver todos los usuarios")
            print("2. Cambiar rol de un usuario")
            print("3. Eliminar un usuario del sistema")
            print("4. Volver al menú principal")
            
            opcion = input("\nElige una acción: ").strip()

            if opcion == "1":
                print("\nListando usuarios del sistema...")
                # Ejemplo de consulta:
                # query = "SELECT numero_documento, nombre_usuario, apellido_usuario, id_rol FROM usuarios"
                # Aquí ejecutas el cursor y haces un for para imprimir los resultados.

            elif opcion == "2":
                doc_usuario = input("Ingresa el número de documento del usuario a modificar: ")
                nuevo_rol = input("Ingresa el nuevo ID de rol (1:Admin, 2:Funcionario, 3:Entrenador, 4:Aprendiz): ")
                
                # query = "UPDATE usuarios SET id_rol = %s WHERE numero_documento = %s"
                # cursor.execute(query, (nuevo_rol, doc_usuario))
                # connect[0].commit()
                print(f"✅ Rol actualizado exitosamente para el documento {doc_usuario}.")

            elif opcion == "3":
                doc_usuario = input("Ingresa el número de documento del usuario que deseas ELIMINAR: ")
                confirmacion = input(f"¿Estás seguro de eliminar el documento {doc_usuario}? (s/n): ").lower()
                
                if confirmacion == 's':
                    # query = "DELETE FROM usuarios WHERE numero_documento = %s"
                    # cursor.execute(query, (doc_usuario,))
                    # connect[0].commit()
                    print("✅ Usuario eliminado correctamente del sistema.")
                else:
                    print("Operación cancelada.")

            elif opcion == "4":
                break
            else:
                print("Opción inválida.")

    def ver_maquinas(self):
        print("\n--- INVENTARIO Y MANTENIMIENTO DE MÁQUINAS ---")
        print("Obteniendo listado de equipos operativos y en mantenimiento...\n")
        
        # Ejemplo de conexión y consulta para el inventario:
        # connect = conexion.connect()
        # cursor = connect[1]
        # query = "SELECT placa_equipo, nombre_equipo, marca, estado, proximo_mantenimiento FROM maquinas"
        # cursor.execute(query)
        # maquinas = cursor.fetchall()
        
        # Simulación de la visualización en base a tu HTML:
        print(f"{'PLACA':<12} | {'MÁQUINA':<35} | {'ESTADO':<15} | {'PRÓXIMO MANT.'}")
        print("-" * 80)
        print(f"{'AG-EQ-001':<12} | {'Banco Plano Olímpico con Soporte':<35} | {'Operativo':<15} | {'2026-09-01'}")
        print(f"{'AG-EQ-002':<12} | {'Caminadora Eléctrica Pro T80':<35} | {'Operativo':<15} | {'2026-09-10'}")
        print(f"{'AG-EQ-003':<12} | {'Máquina Smith Multifuncional':<35} | {'Mantenimiento':<15} | {'2026-08-22'}")
        
        input("\nPresiona ENTER para volver al menú...")