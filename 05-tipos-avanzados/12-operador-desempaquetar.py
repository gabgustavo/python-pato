lista = [1, 2, 3, 4, 5]
print(1, 2, 3, 4, 5)
# * hace lo mismo que en el print
print(*lista)

porAlgunaRazon = ['n1', 'n2', 'n3']


def n(n1, n2, n3):
    return n1 + n2 + n3


print(n(*porAlgunaRazon))

print('-' * 30)

lista2 = [7, 9]

combinada = [*lista, *lista2]

print(combinada)
print('-' * 30)
combinada = ['nuevo', *lista, 'elemento', *lista2, 'en lista']
print(combinada)
print('-' * 30)

print('===DICCIONARIOS===')

usuario1 = {
    "nombre": "Luis"
}
usuario2 = {
    "apellido": "Avila"
}

usuario = {**usuario1, "id": 123, **usuario2, "edad": 38}
print(usuario)
