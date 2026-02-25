class Perro:
    # los metodos magicos siempre inician con 2 __ y terminan con 2 __ y ya estan predefinidos
    # https://rszalski.github.io/magicmethods/

    #  __init__ metodo mágico
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __del__(self):
        print(f"La clase: {self.nombre} ha sido eliminada")

    def __str__(self):
        return f"Clase Perro: {self.nombre}"

    def habla(self):
        print(f"{self.nombre} dice Guau")


perro = Perro("Firulais", 5)
print(perro)
print(perro.nombre)
