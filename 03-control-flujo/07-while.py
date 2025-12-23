numero = 1

while numero < 100:
    print(numero)
    numero *= 2  # numero = numero + 1

print("Escribe salir para terminar el programa")
comando = ""

while comando.lower() != "salir":
    comando = input("$ ")
    print(f"Usted ingresó: {comando}")
