edad = 19

print("_" * 20, 1)

if edad > 17:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

print("_" * 20, 2)

if edad > 17:
    mensaje = "Eres mayor de edad"
else:
    mensaje = "Eres menor de edad"

print(mensaje)

print("_" * 20, '3')

mensaje = "Eres mayor de edad" if edad > 17 else "Eres menor de edad"
print(mensaje)
