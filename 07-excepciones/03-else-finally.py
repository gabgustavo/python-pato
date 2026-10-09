try:
    n1 = int(input("Ingrese el primer número: "))
except Exception as e:
    print("Ocurrió un error :(")
    print("Error:", type(e).__name__)
else:
    print("No ocurrió ningún error")
finally:
    print("Esto se ejecuta siempre")
