numeros = [20, 4, 2, 9, 1, 5, 6, 3, 8, 7]

numeros.sort()  # Ordena la lista en orden ascendente
print(numeros)

numeros.sort(reverse=True)  # Ordena la lista en orden descendente
print(numeros)

numeros = [20, 4, 2, 9, 1, 5, 6, 3, 8, 7]

# Devuelve una nueva lista ordenada en orden ascendente sin modificar la original
sorted(numeros)
numerosNuevo = sorted(numeros)
print(numeros)
print(numerosNuevo)

usuarios = [["Juan", 25],
            ["Ana", 30],
            ["Pedro", 20],
            ["María", 27]
            ]


def ordenar(elemento):
    return elemento[1]


# usuarios.sort()
usuarios.sort(key=ordenar, reverse=True)
print(usuarios)
