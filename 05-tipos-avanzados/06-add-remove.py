mascotas = ["perro",
            "gato",
            "pez",
            "loro",
            "hamster",
            "conejo",
            "perro"
            ]

mascotas.insert(2, "tortuga")  # Inserta en una posición específica (2)
print(mascotas)

mascotas.append("pajaro")  # Agrega al final de la lista
print(mascotas)

# Elimina la primera ocurrencia del valor especificado
mascotas.remove("perro")
print(mascotas)

mascotas.pop()  # Elimina el último elemento
print(mascotas)

mascotas.pop(2)  # Elimina el elemento en la posición 2
print(mascotas)

del mascotas[1]  # Elimina el elemento en la posición 1
print(mascotas)

mascotas.clear()  # Elimina todos los elementos de la lista
print(mascotas)
