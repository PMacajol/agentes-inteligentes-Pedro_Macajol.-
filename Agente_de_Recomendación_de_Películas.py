import random

def recomendador_peliculas():
    # Diccionario de películas organizadas por género
    peliculas_por_genero = {
    "acción": ["Ciudad de Dios", "El infierno", "Carandiru", "Rosario Tijeras", "La hora cero"],
    "comedia": ["Nosotros los Nobles", "Relatos Salvajes", "El hijo de la novia", "La dictadura perfecta", "Un novio para mi mujer"],
    "drama": ["Roma", "Amores Perros", "El secreto de sus ojos", "Y tu mamá también", "Machuca"],
    "ciencia ficción": ["Cronos", "Al final del túnel", "Órbita 9", "Pánico 5 Bravo", "Sleep Dealer"],
    "terror": ["La casa del fin de los tiempos", "Kilómetro 31", "El espinazo del diablo", "Akelarre", "Somos lo que hay"]
}


    # Solicitar al usuario su género favorito
    print("Géneros disponibles: acción, comedia, drama, ciencia ficción, terror")
    genero_favorito = input("¿Cuál es tu género de película favorito? ").lower()

    # Verificar si el género existe en el diccionario
    if genero_favorito in peliculas_por_genero:
        # Seleccionar una película aleatoria del género favorito
        pelicula_recomendada = random.choice(peliculas_por_genero[genero_favorito])
        print(f"\nRecomendación: ¡Deberías ver '{pelicula_recomendada}'!")
    else:
        print("\nLo siento, no tenemos recomendaciones para ese género.")

# Ejecutar el recomendador de películas
recomendador_peliculas()