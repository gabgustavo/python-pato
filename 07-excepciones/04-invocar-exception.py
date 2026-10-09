# https://docs.python.org/3/builtins/exceptions.html#exception-hierarchy
def divicion(n=0):
    if (n == 0):
        raise ZeroDivisionError("No se puede dividir entre cero", f"{n}")

    return 5 / n


try:
    print(divicion(0))
except ZeroDivisionError as e:
    print(e)
