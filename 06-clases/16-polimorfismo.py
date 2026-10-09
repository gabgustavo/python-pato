from abc import ABC, abstractmethod


class Model (ABC):
    @abstractmethod
    def guardar(self):
        pass


class Usuario(Model):
    def guardar(self):
        print('Guardar en BBDD')


class Session(Model):
    def guardar(self):
        print('Guardar en archivo')


# def guardar(entidad):
#    entidad.guardar()

def guardar(entidades):
    for entidad in entidades:
        entidad.guardar()


usuario = Usuario()
session = Session()

# guardar(usuario)
# guardar(session)
# => esto es el polimorfismo, ya que se puede usar la misma función para diferentes tipos de objetos y llamar un metodo en particular
guardar([session, usuario])
