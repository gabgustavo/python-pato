# no se puede modificar las existencias
# Estas se usan para no permitir modificar la informacion accidentalmente

numeros = (1, 2, 3, 4, 5, 6) + (30, 50, 90)
print(numeros)


punto = tuple([1, 5, 10, 15])
print(punto)
print(punto[:3])
primero, segundo, *otros = punto
print(primero, segundo, otros)

# Genera ERROR
# punto[0] = 10
# punto.pop()
