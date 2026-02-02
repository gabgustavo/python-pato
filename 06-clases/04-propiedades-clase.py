class Perro:
    patas = 4  # Propiedad o atributos de clase

    def __init__(self, nombre, edad):
        #    👇🏼 Propiedad o atributos de clase
        self.name = nombre
        self.age = edad

    # Método de la clase y ya dejan de ser llamados funciones
    def habla(self):
        print(f"{self.name} dice: Guau!")


Perro.patas = 6  # Modificando la propiedad de clase para todos los objetos
mi_perro = Perro('Firulais', 3)
mi_perro.patas = 3  # Modificando la propiedad de clase solo para este objeto
mi_perro.habla()
print(Perro.patas)  # Accediendo a la propiedad de clase
print(mi_perro.patas)  # Accediendo a la propiedad de clase a través del objeto
