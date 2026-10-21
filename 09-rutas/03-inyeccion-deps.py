
# import Correa
# import db
# import api
# import graphql

from pathlib import Path

path = Path()
paths = [p for p in path.iterdir() if p.is_dir()]

dependencias = {
    "db": "Base de datos",
    "api": "Esta es la API",
    "graphql": "Este es el GraphQL",
}

# dependencias = {
#    "db": db,
#    "api": api,
#    "graphql": graphql
# }


def load(p):
    # .replace('/', '.') hacer que sea recursivo
    paquete = __import__(str(p).replace('/', '.'))
    try:
        paquete.init(**dependencias)
    except:
        print(f'El paquete "{paquete.__name__}" no tiene un método init()')


list(map(load, paths))


# class Perro:
# def __init__(self):
# def __init__(self, Correa):
# self.correa = Correa()
