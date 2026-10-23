import random
import string


# numero entre 0 y 1
lista = [1, 2, 3, 4, 5, 6, 7]
lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(lista)
print(random.random())
print(random.randint(1, 20))
print(lista)
print(random.choice(lista2))
print(random.choices(lista2, k=3))
print(random.choices("qwertyui56466,.-", k=3))
print(random.choices("qwertyui56466,.-", k=3))

chars = string.ascii_letters
digitos = string.digits
seleccion = "".join(random.choices(chars + digitos, k=20))
print(seleccion)
