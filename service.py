import os

from domain import Pelicula


class CatalogoPeliculas:
    ruta_archivo = 'peliculas.txt'

    def __init__(self, pelicula):
        self._pelicula = pelicula

    @staticmethod
    def agregar_pelicula(*pelicula):
        try:
            lista_peliculas = [l._nombre for l in pelicula]
            lista = open(CatalogoPeliculas.ruta_archivo, 'a', encoding='utf8')
            for l in lista_peliculas:
                lista.write(str(l) + '\n')
        except Exception as e:
            print(e)
        finally:
            print("Cambios guardados".center(50, '-'))
            lista.close()

    @staticmethod
    def listar_peliculas():
        try:
            lista = open(CatalogoPeliculas.ruta_archivo, 'r', encoding='utf8')
            print("Catálogo".center(50, '-'))
            for l in lista:
                print(l)
        except Exception as e:
            print(e)
        finally:
            print("Fin de la lista".center(50, '-'))
            lista.close()

    @staticmethod
    def eliminar():
        print("Eliminando catálogo".center(50, '-'))
        os.remove('peliculas.txt')


if __name__ == '__main__':
    pel1 = Pelicula("Run")
    pel2 = Pelicula("Golden week")
    CatalogoPeliculas.agregar_pelicula(pel1, pel2)
    CatalogoPeliculas.listar_peliculas()
    CatalogoPeliculas.eliminar()