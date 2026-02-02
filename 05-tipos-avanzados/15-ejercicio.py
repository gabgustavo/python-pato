from pprint import pprint
# 1 Crear funcion para eliminar espacios en blanco en un string y retornar una lista de los caracteres restantes
# 2 Contar en un diccionario cuantos se repiten los caracteres de un string
# 3 Ordenar las llaves de un diccionario por el valor que tiene y retirnar una lista que contenga [("a", 3), ("b", 2), ("c", 1),...]
# de una lista de tuplas [("a", 3), ("b", 2), ("c", 4),("d", 1),...] retornar la que tenga mayor valor
# 4 Crear un mensaje que diga: los caracteres que mas se repiten son: a, b, c... y su cantidad es: x, y, z...

# 5 Crear un mensaje que diga:
# los caracteres que mas se repiten con 4 repieticiones son:
# - C
# - D

# 6 Juntar la solucuin de los ejercicios anteriores
# para encontrar los  caracteres que mas se repiten en un string

# R1
string = "Hola mundo este es mi string"


def eliminar_espacios(texto):
    return [char for char in texto if char != ' ']


string_sin_espacios = eliminar_espacios(string)
print(':===String sin espacios:===')
print(string_sin_espacios)

# R2


def contar_caracteres(lista):
    contador = {}
    for char in lista:
        if char in contador:
            contador[char] += 1
        else:
            contador[char] = 1
    return contador


contador_caracteres = contar_caracteres(string_sin_espacios)
print(':===Cantidad de caracteres:===')
pprint(contador_caracteres, width=1)

# R3


def ordenar_diccionario_por_valor(diccionario):
    return sorted(diccionario.items(), key=lambda item: item[1], reverse=True)


caracteres_ordenados = ordenar_diccionario_por_valor(contador_caracteres)
print(':===Caracteres ordenados por cantidad:===')
print(caracteres_ordenados)

# R4


def mayor_tupla(lista):
    maximo = lista[0][1]
    respuesta = {}
    for orden in lista:
        if maximo > orden[1]:
            break
        respuesta[orden[0]] = orden[1]
    return respuesta


caracteres_mayores = mayor_tupla(caracteres_ordenados)
print(':===Caracteres con mayor cantidad:===')
pprint(caracteres_mayores, width=1)

# R5


def crear_mensaje(diccionario):
    mensaje = f'Los caracteres que mas se repiten son:\n'
    for key, char in diccionario.items():
        mensaje += f'- {key} con {char} repeticiones\n'
    return mensaje


mensaje_final = crear_mensaje(caracteres_mayores)
print(':===Mensaje final:===')
print(mensaje_final)
