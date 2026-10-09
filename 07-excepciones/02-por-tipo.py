# print(""

lista = [1, 2, 3, 4, 5]
# IndexError: list index out of range
# lista[45]

# ValueError: invalid literal for int() with base 10: 'j'
# n1 = int(input("Ingrese el primer número: "))

try:
    n1 = int(input("Ingrese el primer número: "))
    asdasdas

except ValueError as e:
    print("Ocurrió un error :(")
    print("Error:", type(e).__name__)

except NameError as e:
    print("Ocurrió un error!")
    print("Error:", type(e).__name__)
