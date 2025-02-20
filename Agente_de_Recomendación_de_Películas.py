import random

def recomendador_peliculas():
    # Diccionario de películas organizadas por género
    peliculas_por_genero = {
        "acción": ["Mad Max: Fury Road", "John Wick", "The Dark Knight", "Inception", "Gladiator"],
        "comedia": ["Superbad", "The Hangover", "Bridesmaids", "Step Brothers", "Dumb and Dumber"],
        "drama": ["The Shawshank Redemption", "Forrest Gump", "The Godfather", "Schindler's List", "Fight Club"],
        "ciencia ficción": ["Blade Runner 2049", "Interstellar", "The Matrix", "Star Wars: Episode IV", "Inception"],
        "terror": ["The Exorcist", "Hereditary", "The Shining", "Get Out", "A Quiet Place"]
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