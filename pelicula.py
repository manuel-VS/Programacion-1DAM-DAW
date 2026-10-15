peliculas = [
    ("Shrek", 90),
    ("Toy Story", 81),
    ("Buscando a Nemo", 100)
]

opcion = -1

while opcion != 0:
    print("\n--- MENÚ DE PELÍCULAS ---")
    print("1. Mostrar películas")
    print("2. Añadir una película")
    print("3. Intentar cambiar la duración de Shrek")
    print("0. Salir")
    opcion = int(input("Elige una opción: "))
    if opcion == 1:
        for pelicula in peliculas:
            print(pelicula[0], "-", pelicula[1], "minutos")
    elif opcion == 2:
        peliculas.append(("Los Increíbles", 115))
        print("Película añadida correctamente.")
    elif opcion == 3:
        # Las tuplas no permiten modificar sus elementos
        print("No se puede cambiar la duración directamente porque es una tupla.")
    elif opcion == 0:
        print("Saliendo del programa...")
    else:
        print("Opción no válida. Inténtalo de nuevo.")
