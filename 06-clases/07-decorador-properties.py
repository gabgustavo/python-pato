class Perro:

    def __init__(self, nombre):
        self.name = nombre

    @property
    def name(self):
        print(':: getter ::')
        return self.__name

    @name.setter
    def name(self, nombre):
        print(':: setter ::')
        if nombre.strip():
            self.__name = nombre
        return


miperro = Perro('Firulais')
print(miperro.name)
miperro.name = 'Camaron'
print(miperro.name)
