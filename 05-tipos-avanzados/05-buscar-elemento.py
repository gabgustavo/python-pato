mascotas = ["perro", "gato", "pez", "loro", "hamster", "conejo", "perro"]

print(mascotas.index("loro"))  # Devuelve 3
# print(mascotas.index("asd"))  # Lanza ValueError: 'asd' is not in list

if "asd" in mascotas:
    print(mascotas.index("asd"))
else:
    print("El elemento no se encuentra en la lista")


print('-' * 30)
print(mascotas.index("perro"))  # Devuelve 0 (la primera ocurrencia)

print('-' * 30)
print(mascotas.count("perro"))
