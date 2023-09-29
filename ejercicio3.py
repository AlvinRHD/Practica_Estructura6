class Estudiante:
    def __init__(self, nombre, apellido, carnet, carrera):
        # Inicializar los atributos del estudiante
        self.nombre = nombre
        self.apellido = apellido
        self.carnet = carnet
        self.carrera = carrera

    def actualizar_nombre(self, nuevo_nombre):
        # Actualizar el nombre del estudiante
        self.nombre = nuevo_nombre

    def actualizar_apellido(self, nuevo_apellido):
        # Actualizar el apellido del estudiante
        self.apellido = nuevo_apellido

    def actualizar_carnet(self, nuevo_carnet):
        # Actualizar el carnet del estudiante
        self.carnet = nuevo_carnet

    def actualizar_carrera(self, nueva_carrera):
        # Actualizar la carrera del estudiante
        self.carrera = nueva_carrera

    def __str__(self):
        # Devolver una representación en cadena del estudiante
        return f"Nombre: {self.nombre} {self.apellido}\nCarnet: {self.carnet}\nCarrera: {self.carrera}"

# Ejemplo de uso
estudiante1 = Estudiante("Alvin", "Rosales", "U20230560", "Tec. En Desarrollo de Soft.")
print(estudiante1)
estudiante1.actualizar_nombre("Alvin")
estudiante1.actualizar_carnet("u20230560")
print(estudiante1)
