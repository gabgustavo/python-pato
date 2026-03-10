from abc import ABC, abstractmethod


class Model(ABC):
    # tabla = False

    @property
    @abstractmethod
    def tabla(self):
        pass

    @abstractmethod
    def guardar(self):
        # print(f"Guardando {self.tabla} en BBDD")
        pass

    @classmethod
    def findById(self, _id):
        print(f"Buscando por id: {_id} en {self.tabla}")


# model = Model()  # No se puede instanciar una clase abstracta, da error


class Usuario(Model):
    tabla = "usuarios"

    def guardar(self):
        print(f"Guardando {self.tabla} en BBDD")


usuario = Usuario()
usuario.guardar()
Usuario.findById(2)
