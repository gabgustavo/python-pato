import json
from pathlib import Path


# personas = [
#    {"id": 1, "nombre": "Andrés Martínez"},
#    {"id": 2, "nombre": "Laura Rodríguez"},
#    {"id": 3, "nombre": "Carlos Gómez"},
#    {"id": 4, "nombre": "María Fernández"},
#    {"id": 5, "nombre": "Juan Pérez"},
#    {"id": 6, "nombre": "Sofía Ramírez"},
#    {"id": 7, "nombre": "Daniel Torres"},
#    {"id": 8, "nombre": "Valentina Castro"},
#    {"id": 9, "nombre": "Santiago Herrera"},
#    {"id": 10, "nombre": "Camila Moreno"},
#    {"id": 11, "nombre": "Mateo Vargas"},
#    {"id": 12, "nombre": "Isabella Rojas"},
#    {"id": 13, "nombre": "Sebastián Díaz"},
#    {"id": 14, "nombre": "Gabriela Ortiz"},
#    {"id": 15, "nombre": "Nicolás Jiménez"},
#    {"id": 16, "nombre": "Daniela Muñoz"},
#    {"id": 17, "nombre": "Alejandro Silva"},
#    {"id": 18, "nombre": "Mariana Suárez"},
#    {"id": 19, "nombre": "Felipe Romero"},
#    {"id": 20, "nombre": "Lucía Mendoza"}
# ]

# data = json.dumps(personas)
# print(data)

# Path("10-archivos/personas.json").write_text(data)


# Leer json
data = Path("10-archivos/personas.json").read_text(encoding='utf-8')
personal = json.loads(data)
print(personal)


# Modificar json
personal[1]['nombre'] = 'Frank Suarez'
Path("10-archivos/personas.json").write_text(json.dumps(personal))
