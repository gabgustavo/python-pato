def hola():
    print("Hola desde una función")
    print("Una segunda linea dentro de la función")


hola()


def holaArgumento(nombre, apellido):  # función con parametro
    print(f"\nHola {nombre} {apellido} desde una función con argumento")


holaArgumento("Luis", "Avila")  # argumento que se pasa a la función


def holaArgumentoOpcional(nombre, apellido="Beltran"):  # función con parametro
    print(f"\nHola {nombre} {apellido} desde una función con argumento")


holaArgumentoOpcional("Luis")  # argumento opcional

# argumento opcional nombrado
holaArgumentoOpcional(apellido="Barbosa", nombre="Ana")
