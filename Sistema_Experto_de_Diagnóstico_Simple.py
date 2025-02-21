def sistema_experto():
    print("Bienvenido al Sistema Experto de Diagnóstico Simple")
    print("Por favor, responde 'si' o 'no' a los siguientes sintomas:\n")

    # Solicitar sintomas al usuario
    fiebre = input("¿Tienes fiebre? (si/no): ").lower() == "si"
    tos = input("¿Tienes tos? (si/no): ").lower() == "si"
    dolor_garganta = input("¿Tienes dolor de garganta? (si/no): ").lower() == "si"
    dificultad_respirar = input("¿Tienes dificultad para respirar? (si/no): ").lower() == "si"
    fatiga = input("¿Te sientes fatigado/a? (si/no): ").lower() == "si"

    # Lista de diagnósticos posibles
    diagnosticos = []

    # Aplicar reglas de diagnóstico
    if fiebre and tos and dolor_garganta:
        diagnosticos.append("Podrías tener un resfriado común.")
    if fiebre and tos and dificultad_respirar:
        diagnosticos.append("Podrías tener neumonía. Debes consultar a un médico.")
    if fiebre and fatiga and dificultad_respirar:
        diagnosticos.append("Podrías tener COVID-19. Debes hacerte una prueba y aislarte.")
    if dolor_garganta and fatiga:
        diagnosticos.append("Podrías tener faringitis.")
    if fiebre and tos:
        diagnosticos.append("Podrías tener gripe.")
    if fiebre and fatiga:
        diagnosticos.append("Podrías estar deshidratado o con una infección viral.")

    # Mostrar diagnóstico
    if diagnosticos:
        print("\nDiagnóstico:")
        for d in diagnosticos:
            print(f"➡ {d}")
    else:
        print("\nDiagnóstico: Tus sintomas no coinciden con una enfermedad específica, consulta a un médico.")

# Ejecutar el sistema experto
sistema_experto()
