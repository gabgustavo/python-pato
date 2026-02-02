usuarios = [["Juan", 25],
            ["Ana", 30],
            ["Pedro", 20],
            ["María", 27]
            ]


def ordenar(elemento):
    return elemento[1]


# usuarios.sort(key=ordenar, reverse=True)
# usuarios.sort(key=lambda parametros: contenidoFuncion, reverse=True)
usuarios.sort(key=lambda elemento: elemento[1], reverse=True)
# cuando se usan las funciones lambda se evita definir las funciones y todo lo que conlleva
print(usuarios)
