class Perro:

    def __init__(self, nombre, edad):
        self.__name = nombre
        self.__age = edad

    def habla(self):
        print(f"{self.__name} dice: Guau!")

    @classmethod
    def factory(cls):
        return cls("Cachorro", 3)

    def get_name(self):
        return self.__name

    def set_name(self, nuevo_nombre):
        self.__name = nuevo_nombre


perro = Perro.factory()
perro.habla()
# print(perro.__name)
print(perro.get_name())
perro.set_name("Max")
print(perro.get_name())
print(perro.__dict__)  # Muestra las propiedades del objeto
