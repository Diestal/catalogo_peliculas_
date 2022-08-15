class Pelicula:
    def __init__(self, nombre):
        self._nombre = nombre

    def __str__(self):
        return f"Película: {self._nombre}"

if __name__ == "__main__":
    pelicula1 = Pelicula("Chihiro")
    print(pelicula1)