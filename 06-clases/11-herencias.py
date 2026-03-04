class Animal:
    def pasear(self):
        print("Paseando")


class Perro (Animal):
    def comer(self):
        print("Comiendo")


class Gato(Perro):

    def programar(self):
        print("El gato está programando")


perro = Perro()
perro.pasear()
perro.comer()
print("_" * 20)
gato = Gato()
gato.pasear()
gato.programar()
