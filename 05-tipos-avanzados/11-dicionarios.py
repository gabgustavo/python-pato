usuario = {
    "nombre": "Luis",
    "apellido": "Avila",
    "edad": 38,
}
print('-' * 30, '>Dicionario<')
print(usuario)
print(usuario["nombre"] + " " + usuario["apellido"])

print('-' * 30, '>Agregando una nueva propiedad<')
usuario['email'] = 'luis.avila@gmail.com'
print(usuario)

# aqui si una propiedad no existe genera error
if "doc" in usuario:
    print(f"El documento de {usuario['nombre']} es: {usuario['doc']}")

print('-' * 30, '>get<')
print(usuario.get('nombre'))

# en get no se presenta error, se obtiene un None, pero se puede pasar un valor default
print(usuario.get('doc', 'Valor por defecto'))

# eliminacion
print('-' * 30, '>eliminado<')
del usuario['email']
print(usuario)
del (usuario['edad'])
print(usuario)

usuario['doc'] = 123456789
print('-' * 30, '>for en dicionario<')
for item in usuario:
    print(f"{item}: {usuario[item]}")


print('-' * 30, '>for 2<')
for item in usuario.items():
    print(item)
print('-' * 30)
for key, value in usuario.items():
    print(f"key: {key}, value: {value}")

usuarios = [
    {
        "id": 1,
        "nombre": "Luis",
        "apellido": "Avila",
        "edad": 38,
    },
    {
        "id": 2,
        "nombre": "Juan",
        "apellido": "Roncón",
        "edad": 15,
    },
    {
        "id": 3,
        "nombre": "Patricia",
        "apellido": "Avila",
        "edad": 25,
    }
]

print("====Usuarios====")
for user in usuarios:
    print(f"""
        Id: {user['id']}
        Nombre: {user['nombre']}
        Apellido: {user['apellido']}
        Edad: {user['edad']}
    __________""")
