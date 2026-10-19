import time
import usuarios.conexion as conexion

class MenuFuncionario:
    # Es necesario recibir el documento para poder buscar su rutina en la BD
    def __init__(self, nombre_usuario, numero_documento):
        self.nombre_usuario = nombre_usuario
        self.numero_documento = numero_documento

    def iniciar(self):
        while True:
            print("\n" + "="*60)
            print(f" BIENVENIDO FUNCIONARIO: {self.nombre_usuario.upper()} ".center(60))
            print("="*60)
            print("1. Mis Rutinas")
            print("2. Módulo Operativo: Aseo y Vigilancia")
            print("3. Salir")
            print("="*60)

            opcion = input("Elige una opción (1-3): ")

            if opcion == "1":
                self.ver_rutinas()
            elif opcion == "2":
                self.modulo_operativo()
            elif opcion == "3":
                print("\nCerrando sesión del portal funcionario. ¡Hasta pronto!")
                break
            else:
                print("\nOpción no válida. Intenta de nuevo.")

    def ver_rutinas(self):
        print("\n" + "-"*40)
        print(" MIS RUTINAS ".center(40))
        print("-" * 40)

        try:
            connect = conexion.connect()
            cursor = connect[1]
            
            # Reutilizamos la misma consulta que usa el aprendiz
            sql = """
                SELECT ar.nombre_asignacion 
                FROM asignacion_rutinas ar
                JOIN usuarios u ON ar.id_usuario = u.id_usuario
                WHERE u.numero_documento = %s
            """
            cursor.execute(sql, (self.numero_documento,))
            resultado = cursor.fetchone()
            
            if resultado:
                print(f"\nRutina asignada por el instructor: >> {resultado[0].upper()} <<")
            else:
                print("\nActualmente no tienes ninguna rutina asignada.")
                
        except Exception as e:
            print(f"Error al consultar la rutina en la base de datos: {e}")
            
        input("\nPresiona Enter para volver al menú...")

    def modulo_operativo(self):
        while True:
            print("\n" + "-"*60)
            print(" MÓDULO OPERATIVO: ASEO Y VIGILANCIA ".center(60))
            print("-" * 60)
            print("1. Checklist de Áreas y Equipos (Desinfección)")
            print("2. Consultar Insumos de Bioseguridad")
            print("3. Libro de Minutas y Reporte de Novedades")
            print("4. Volver al menú principal")
            
            opcion = input("\nSelecciona una opción (1-4): ")

            if opcion == "1":
                print("\n--- CHECKLIST DE DESINFECCIÓN ---")
                print("[ ] Zona de Cardio (Alta prioridad)")
                print("[ ] Zona de Peso Libre (Alta prioridad)")
                print("[ ] Máquinas de Fuerza (Media prioridad)")
                input("\nPresiona Enter para marcar áreas o volver...")
                
            elif opcion == "2":
                print("\n--- ESTADO DE INSUMOS ---")
                print("- Alcohol Antiséptico 70%: 12 Galones (Óptimo)")
                print("- Jabón Líquido Antibacterial: 6 Litros (Óptimo)")
                print("- Paños de Microfibra: 15 Unidades (Regular)")
                input("\nPresiona Enter para continuar...")
                
            elif opcion == "3":
                novedad = input("\nEscribe el reporte de novedad o minuta del turno: ")
                print("\nRegistrando novedad...")
                time.sleep(1)
                print(f"¡Novedad registrada exitosamente bajo el usuario {self.nombre_usuario}!")
                
            elif opcion == "4":
                break
            else:
                print("\nOpción no válida.")