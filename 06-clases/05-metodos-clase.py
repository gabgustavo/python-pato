class Perro:
    patas = 4  # Propiedad o atributos de clase

    def __init__(self, nombre, edad):
        #    👇🏼 Propiedad o atributos de clase
        self.name = nombre
        self.age = edad

    # cls: se refiere a la clase misma
    @classmethod
    def habla(cls):
        print(f"Guau!")

    @classmethod
    def factory(cls):
        return cls("Cachorro", 3)


Perro.habla()
cachorro = Perro.factory()
print(cachorro.name, cachorro.age)
