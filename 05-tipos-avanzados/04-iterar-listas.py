mascotas = ["perro", "gato", "pez", "loro", "hamster", "conejo"]

for mascota in mascotas:
    print(mascota)

print('-' * 30)

for mascota in enumerate(mascotas):  # tuplas
    print(mascota)
    print(f"> Índice: {mascota[0]}, Mascota: {mascota[1]}")

print('-' * 30)

for index, mascota in enumerate(mascotas):
    print(f"> Índice: {index}, Mascota: {mascota}")
