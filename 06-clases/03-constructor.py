class Perro:
    def __init__(self, nombre, edad):
        self.name = nombre
        self.age = edad

    # Método de la clase y ya dejan de ser llamados funciones
    def habla(self):
        print(f"{self.name} dice: Guau!")


mi_perro = Perro('Firulais', 3)
mi_perro.habla()
