# No es recomendable usar variables globales
VariableGlobal = "Soy una variable global"


def saludar():
    global VariableGlobal  # aacesar a la variable global
    mensaje = "¡Hola, mundo! " + VariableGlobal
    print(mensaje)


def saludarAlDeveloper():
    mensaje = "¡Hola, desarrollador!"
    print(mensaje)


print(VariableGlobal)
saludar()
