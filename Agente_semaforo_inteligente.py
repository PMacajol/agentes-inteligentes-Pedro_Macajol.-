import time
import random

class SemaforoInteligente:
    def __init__(semaforo):
        semaforo.estado = "rojo"  # Estado inicial del semáforo
        semaforo.tiempo_verde = 10  
        semaforo.tiempo_amarillo = 3  
        semaforo.tiempo_rojo = 5  

    def trafico(semaforo):
        # Simula la detección de vehículos (número aleatorio entre 0 y 20)
        return random.randint(0, 20)

    def tiempos(semaforo, vehiculos):
        # Ajusta el tiempo en verde según el número de vehículos detectados
        if vehiculos < 5:
            semaforo.tiempo_verde = 5  # Poco tráfico, tiempo corto en verde
        elif 5 <= vehiculos < 15:
            semaforo.tiempo_verde = 10  # Tráfico moderado, tiempo medio en verde
        else:
            semaforo.tiempo_verde = 15  # Mucho tráfico, tiempo largo en verde

    def cambiar_estado(semaforo):
        # Cambia el estado del semáforo y muestra el estado actual
        if semaforo.estado == "verde":
            semaforo.estado = "amarillo"
            tiempo_espera = semaforo.tiempo_amarillo
        elif semaforo.estado == "amarillo":
            semaforo.estado = "rojo"
            tiempo_espera = semaforo.tiempo_rojo
        else:
            semaforo.estado = "verde"
            tiempo_espera = semaforo.tiempo_verde

        print(f"El semáforo está en {semaforo.estado} durante {tiempo_espera} segundos.")
        time.sleep(tiempo_espera)

    def ejecutar(semaforo):
        while True:
            vehiculos = semaforo.trafico()
            print(f"Vehículos detectados: {vehiculos}")
            semaforo.tiempos(vehiculos)
            semaforo.cambiar_estado()


# Crear una instancia del semáforo y ejecutar el programa
semaforo = SemaforoInteligente()
semaforo.ejecutar()