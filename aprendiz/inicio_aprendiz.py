import time

class MenuAprendiz:
    # Fíjate bien en los dobles guiones bajos: __init__
    def __init__(self, nombre_usuario, numero_documento, dias_adaptacion):
        self.nombre_usuario = nombre_usuario
        self.numero_documento = numero_documento
        self.dias_adaptacion = int(dias_adaptacion)
        self.rutina_instructor = ""

    def iniciar(self):
        # Ahora la línea 17 funcionará perfectamente porque dias_adaptacion es un número:
        progreso_pct = int((self.dias_adaptacion / 5) * 100)
        # ... resto de tu código original ...

    def iniciar(self):
        while True:
            print("\n" + "="*70)
            print(f" ROL APRENDIZ SENA • ETAPA INDUCTIVA ".center(70, "="))
            print("="*70)
            
            # --- Barra de progreso de la imagen ---
            progreso_pct = int((self.dias_adaptacion / 5) * 100)
            print(f" Progreso de Adaptación: {progreso_pct}% ".center(70))
            print(f" {self.dias_adaptacion} de 5 Días Realizados ".center(70))
            
            if self.dias_adaptacion < 5:
                print(f" [!] Rutinas Asignadas Bloqueadas (Faltan {5 - self.dias_adaptacion} días) ".center(70))
            else:
                print(" [✓] Rutinas Desbloqueadas ".center(70))
            print("="*70)
            
            print("1. Semana de Adaptación al Gimnasio CBA")
            print("2. Ver Rutinas Asignadas por el Instructor")
            print("3. Salir")
            print("-" * 70)

            opcion = input("Elige una opción (1-3): ")

            if opcion == "1":
                self.ver_semana_adaptacion()
            elif opcion == "2":
                self.ver_rutinas()
            elif opcion == "3":
                print(f"\nCerrando sesión del portal. ¡Hasta pronto {self.nombre_usuario}!")
                break
            else:
                print("\nOpción no válida. Intenta de nuevo.")

    def ver_semana_adaptacion(self):
        while True:
            print("\n" + "*"*70)
            print(" SEMANA DE ADAPTACIÓN AL GIMNASIO CBA ".center(70))
            print("*" * 70)
            print("Programa de 5 días diseñado para aprender el uso seguro de las")
            print("máquinas, biomecánica correcta y hábitos saludables.")
            print("-" * 70)
            print(" CRONOGRAMA:")
            
            # Textos exactos sacados de tu diseño frontend
            dias = [
                ("DÍA 1", "Inducción & Calentamiento General", "40 min • Baja"),
                ("DÍA 2", "Tren Superior & Máquinas Guiadas", "45 min • Baja-Media"),
                ("DÍA 3", "Tren Inferior & Prevención Articular", "45 min • Media"),
                ("DÍA 4", "Zona Media (Core) & Estabilidad", "40 min • Baja-Media"),
                ("DÍA 5", "Circuito Integrado & Evaluación", "50 min • Media")
            ]
            
            for i, (dia, titulo, desc) in enumerate(dias):
                estado = "[✓] COMPLETADO" if i < self.dias_adaptacion else "[ ] PENDIENTE "
                print(f"{estado} | {dia}: {titulo} ({desc})")
            print("-" * 70)
            
            print("\nOpciones:")
            if self.dias_adaptacion < 5:
                # Opción sacada del botón verde de tu imagen
                print(f"1. Entrenar {dias[self.dias_adaptacion][0]} con Temporizador")
            print("2. Volver al menú principal")
            
            opc = input("Selecciona: ")
            
            if opc == "1" and self.dias_adaptacion < 5:
                dia_actual = dias[self.dias_adaptacion][0]
                print(f"\nIniciando {dia_actual}... (Simulando entrenamiento de 45 min)")
                time.sleep(2)
                print("¡Entrenamiento finalizado con éxito! Progreso guardado.")
                self.dias_adaptacion += 1
                time.sleep(1)
            elif opc == "2":
                break
            else:
                print("\nOpción no válida.")

    def ver_rutinas(self):
        # --- AQUÍ PEGAS TODO EL BLOQUE NUEVO DE LA IMAGEN ---
        import usuarios.conexion as conexion 
        try:
            connect = conexion.connect()
            cursor = connect[1]
            # Consulta relacionada entre asignacion_rutinas y usuarios
            sql = """
                SELECT ar.nombre_asignacion 
                FROM asignacion_rutinas ar
                JOIN usuarios u ON ar.id_usuario = u.id_usuario
                WHERE u.numero_documento = %s
            """
            cursor.execute(sql, (self.numero_documento,))
            resultado = cursor.fetchone()
            
            if resultado:
                self.rutina_instructor = resultado[0] 
            else:
                self.rutina_instructor = "" 
                
        except Exception as e:
            print(f"Error al consultar la rutina en la base de datos: {e}")
            self.rutina_instructor = ""

        # Si aún no termina la semana de adaptación, no lo deja ver las rutinas
        if self.dias_adaptacion < 5:
            print("ESTADO: Rutinas bloqueadas.")
            print("Debes completar los 5 días de la semana de adaptación primero.")
        
        # Si ya terminó los 5 días, revisa si el instructor dejó una rutina
        elif self.rutina_instructor and self.rutina_instructor.strip() != "":
            print("Tu plan actual asignado por el instructor es:")
            print(f"-> {self.rutina_instructor}")
            
        # Si ya terminó los 5 días pero el instructor no ha asignado nada
        else:
            print("NO DISPONIBLE O PRÓXIMAMENTE.")
            print("Tu instructor aún no ha cargado una rutina personalizada.")
        
        time.sleep(2)