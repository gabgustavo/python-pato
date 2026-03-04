class Animal:
    def pasear(self):
        print("Paseando animales")

    def comer(self):
        print("Comiendo")


class Perro:
    def comer(self):
        print("El perro está comiendo")


class Gato(Perro, Animal):

    def programar(self):
        print("El gato está programando")


gato = Gato()
gato.pasear()
gato.comer()
gato.programar()

perro = Perro()
perro.comer()
