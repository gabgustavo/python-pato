
numeros = [1, 2, 3]

# Feo!!!
"""primero = numeros[0]
segundo = numeros[1]
tercero = numeros[2]"""

# Bien
primero, segundo, tercero = numeros
print(primero, segundo, tercero)

# Extraer el primer elemento y el resto en otra lista
n1, *otros = numeros

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

primero, segundo, *otros = numeros
print(primero, segundo, otros)
primero, *otros, ultimo = numeros
print(primero, otros, ultimo)
