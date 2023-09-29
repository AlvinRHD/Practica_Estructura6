class Biblioteca:
    def __init__(self, _libros):
        self.libros = _libros

        #mostrar libros
        def mostrarLibros(self):
            for libro in self.libros:
                print(libro)

        def prestarLibros(self, nombreLibros):
            #verificar si el libro existe
            if nombreLibros in self.libros:
                print("Se presto el libro", nombreLibros)
                self.libros.remove(nombreLibros)
            else:
                print("El libro no existe")

        def agregarLibro(self, nombreLibros):
            #verificar que no exista
            if nombreLibros not in self.libros:
                print("Se añadio el libro", nombreLibros)
                self.libros.append(nombreLibros)
            else:
                print("El libro ya existe")


libros = ["Clean Code", "Java", "Analisis"]

biblioteca = Biblioteca(libros)

while True:
    print("1) Agregar libro")
    print("2) Presentar libro")
    print("3) Mostrar libro")
    print("4) Salir")

    opcion = int(input("Ingres un opcion(1-4)"))

    if opcion == 1:
        libro = input("\nIngresa el nombre del libro")
        biblioteca.agregarLibro(libro)
    elif opcion == 2:
        libro = input("\nIngresa el nombre del libro")
        biblioteca.prestarLibros(libro)
    elif opcion == 3:
        print("\nMis libros son")
        biblioteca.MostrarLibros(libro)
    elif opcion == 4:
        break