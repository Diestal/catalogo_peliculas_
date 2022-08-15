from domain import Pelicula
from service import CatalogoPeliculas as CP

flag = True
msg = ('''
        Opciones:
        1. Agregar pelicula
        2. Listar pelicula
        3. Eliminar catálogo de películas
        4. Salir
        '''
          )


while flag:
    print(msg)
    user_opt = int(input("Escribe tu opción: "))
    if user_opt == 1:
        user_pelicula = input('\nProporciona la película: ')
        pelicula = Pelicula(user_pelicula)
        CP.agregar_pelicula(pelicula)
    elif user_opt == 2:
        CP.listar_peliculas()
    elif user_opt == 3:
        CP.eliminar()
    elif user_opt == 4:
        print("Saliendo...")
        flag = False

