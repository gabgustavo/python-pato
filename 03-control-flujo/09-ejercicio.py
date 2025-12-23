print("=" * 50)
print("Bienvenido al la aplicacion de calculadora")
print("=" * 50)
print("Para salir escriba 'salir' en cualquier momento")
print("Las operaciones disponibles son: suma, resta, multi, div")

primerNumero = None

while True:

    if primerNumero is None:
        primerNumero = input("Ingrese el primer numero: ")

        if primerNumero.lower() == "salir":
            print("Saliendo de la calculadora...")
            break
        primerNumero = int(primerNumero)

    operacion = input("Ingrese la operación a realizar: ")

    if operacion.lower() == "salir":
        print("Saliendo de la calculadora...")
        break

    segundoNumero = input("Ingrese el segundo numero: ")
    if segundoNumero.lower() == "salir":
        print("Saliendo de la calculadora...")
        break
    segundoNumero = int(segundoNumero)

    if operacion.lower() == "suma":
        resultado = primerNumero + segundoNumero
        primerNumero = resultado

    elif operacion.lower() == "resta":
        resultado = primerNumero - segundoNumero
        primerNumero = resultado

    elif operacion.lower() == "multi":
        resultado = primerNumero * segundoNumero
        primerNumero = resultado

    elif operacion.lower() == "div":
        if segundoNumero == 0:
            print("Error: No se puede dividir por cero")
            break
        resultado = primerNumero / segundoNumero
        primerNumero = resultado
    else:
        print("Operación no reconocida, intente de nuevo")
        break

    print(f"El resultado es: {resultado}")
