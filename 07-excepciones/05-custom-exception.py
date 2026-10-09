class MiError(Exception):
    "Esta clase es para representar un error personalizado"

    def __init__(self, mensaje, codigo):
        self.mensaje = mensaje
        self.codigo = codigo

    def __str__(self):
        return f"{self.mensaje} - Código: {self.codigo}"


def divicion(n=0):
    if (n == 0):
        raise MiError("No se puede dividir entre cero", f"{n}")

    return 5 / n


try:
    print(divicion(0))
except MiError as e:
    # print(e)
    # print(f"Error: {e.mensaje}, Código: {e.codigo}")
    print(e)
