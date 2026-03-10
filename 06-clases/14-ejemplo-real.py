class Model():
    tabla = False

    def __init__(self):
        if not self.tabla:
            print("Error: No se ha definido la tabla para el modelo")

    def guardar(self):
        print(f"Guardando {self.tabla} en BBDD")

    @classmethod
    def findById(self, _id):
        print(f"Buscando por id: {_id} en {self.tabla}")


class Usuario(Model):
    tabla = "usuarios"


usuario = Usuario()
usuario.guardar()
Usuario.findById(2)
