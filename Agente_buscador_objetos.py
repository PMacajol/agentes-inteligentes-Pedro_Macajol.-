import random
import time

class AgenteBuscador:
    def __init__(agente, tamaño_cuadricula=5):
        agente.tamaño_cuadricula = tamaño_cuadricula
        agente.cuadricula = [[' ' for _ in range(tamaño_cuadricula)] for _ in range(tamaño_cuadricula)]
        agente.agente_pos = (0, 0)  # Posición inicial
        agente.objeto_pos = agente.generar_objeto_pos()  # Posición aleatoria del objeto
        agente.cuadricula[agente.agente_pos[0]][agente.agente_pos[1]] = 'A'  # Marcar agente
        agente.cuadricula[agente.objeto_pos[0]][agente.objeto_pos[1]] = 'O'  # Marcar objeto

    def generar_objeto_pos(agente):
        while True:
            pos = (random.randint(0, agente.tamaño_cuadricula - 1), random.randint(0, agente.tamaño_cuadricula - 1))
            if pos != agente.agente_pos:
                return pos

    def mostrar_cuadricula(agente):
        for fila in agente.cuadricula:
            print("|" + "|".join(fila) + "|")
        print()

    def mover_agente(agente):
        while agente.agente_pos != agente.objeto_pos:
            fila_diff = agente.objeto_pos[0] - agente.agente_pos[0]
            columna_diff = agente.objeto_pos[1] - agente.agente_pos[1]

            if fila_diff != 0:
                nueva_fila = agente.agente_pos[0] + (1 if fila_diff > 0 else -1)
                nueva_columna = agente.agente_pos[1]
            else:
                nueva_fila = agente.agente_pos[0]
                nueva_columna = agente.agente_pos[1] + (1 if columna_diff > 0 else -1)

            agente.cuadricula[agente.agente_pos[0]][agente.agente_pos[1]] = ' '  # Borrar posición anterior
            agente.agente_pos = (nueva_fila, nueva_columna)
            agente.cuadricula[agente.agente_pos[0]][agente.agente_pos[1]] = 'A'  # Nueva posición

            print(f"Movimiento hacia: {agente.agente_pos}")
            agente.mostrar_cuadricula()
            time.sleep(1)

        print("¡Objeto encontrado!")

# Crear una instancia y ejecutar el programa
agente = AgenteBuscador()
print("Cuadrícula inicial:")
agente.mostrar_cuadricula()
agente.mover_agente()
