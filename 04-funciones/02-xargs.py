def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma(3, 5)
suma(3, 5, 7, 9, 20)
suma(3, 5, 30, 50, 70, 90, 100)
