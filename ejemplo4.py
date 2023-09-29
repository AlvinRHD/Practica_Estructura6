class Perro:
    def sonido(self):
        print("Guauuuuuuuuu!!")

class Gato:
    def sonido(self):
        print("Miauuuuuuuuu!!")

class Vaca:
    def sonido(self):
        print("Muuuuuuuuuu!!")
# perro1 = Perro()
# gato1 = Gato()
# vaca1 = Vaca()

misPersonajes = []

for i in range(0, 10):
    if i%2==0:
        misPersonajes.append(Perro())
    elif (i+1)%3==0:
        misPersonajes.append(Vaca())
    else:
        misPersonajes.append(Gato())

for animal in misPersonajes:
    animal.sonido()

