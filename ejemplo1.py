# creando una clase
class Personas:
    nombre = ""
    apellido = ""
    genero = ""
    edad = ""
    estado_civil = ""


    def __init__(self, _nombre, _apellido, _genero):
        self.nombre = _nombre
        self.apellido = _apellido
        self.genero = _genero

    #Metodo
    def hablar(self, mensaje):
        print (mensaje)

#creando un objeto
#objeto es una instancia de la clase
#instanciar es crear un objeti a partir de una clase

persona1 = Personas("Alvin", "Rosales", "M")
persona2 = Personas("Ezequiel", "Hernández", "M")



print(f"{persona1.nombre} {persona1.apellido}")
print(f"{persona2.nombre} {persona2.apellido}")