nombre = "Luis"
apellido = "Avila"
nombreCompleto = nombre + " " + apellido  # No es lo mas adecuado
print(nombreCompleto)
nombreCompleto = f"{nombre} {apellido}"
print(nombreCompleto)  # Salida: Luis Avila

nuevoFormato = f"{nombre[0]} {4 * 5}"
print(nuevoFormato)
