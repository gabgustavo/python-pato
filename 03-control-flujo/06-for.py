for numero in range(5):
    print(numero)


print("_" * 20)
buscar = 10
for numero in range(5):
    print('??? ', numero)
    if numero == buscar:
        print("¡Lo encontré!", numero)
        break
else:  # else del for
    print("No lo encontré nada :(")


# Iteralbles
# - range
# - strings
# - listas
# - tuplas
# - diccionarios

string = "Este es un string"
for letra in string:
    print(f"estamos en la letra: \"{letra}\" de ({string})")
