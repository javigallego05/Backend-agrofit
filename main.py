from usuarios import acciones

while True:
    print("""
    ======================================
        SISTEMA DE GESTIÓN AGROFIT
    ======================================
    Acciones disponibles:
        1. Registro
        2. Login
        3. Recuperacion
        4. Salir
    """)

    hazEl = acciones.Acciones()
    opcion = input("¿Qué quieres hacer? (elige el número o escribe la acción): ").strip().lower()

    if opcion in ["1", "registro"]:
        hazEl.registro()
    elif opcion in ["2", "login"]:
        hazEl.login()
    elif opcion in ["3", "recuperacion"]:
        hazEl.recovery()
    elif opcion in ["4", "salir"]:
        print("\n¡Gracias por usar Agrofit! Hasta pronto.")
        break
    else:
        print("\nOpción no válida.")