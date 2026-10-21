from datetime import datetime
from io import open


# escritura
texto = "Esta es una escriptura\nde prueba con open"
archivo = open("10-archivos/archivo-open.txt", "w", encoding="utf-8")
archivo.write(texto)
archivo.close()

# lectura
# archivo = open("10-archivos/archivo-open.txt", "r", encoding="utf-8")
# texto = archivo.read()
# archivo.close()
# print(texto)

# lectura como lista
# archivo = open("10-archivos/archivo-open.txt", "r", encoding="utf-8")
# lineas = archivo.readlines()
# archivo.close()
# print(lineas)


# __enter__ y __exit__ abre el archi y lo cierra automáticamente
# with open("10-archivos/archivo-open.txt", "r", encoding="utf-8") as archivo:
# lee todo el archivo en memoria
# lineas = archivo.readlines()
# print(lineas)

# retroceder el cursor al inicio del archivo
# archivo.seek(0)

# este carga de una linea a la vez, no carga todo el archivo en memoria
# for linea in archivo:
#    print(linea)


# Agregar
# archivo = open("10-archivos/archivo-open.txt", "a+", encoding="utf-8")
# archivo.write("\nEsta es una línea agregada")
# archivo.close()

# Lectura y escritura
with open("10-archivos/archivo-open.txt", "r+", encoding="utf-8") as archivo:
    texto = archivo.readlines()
    archivo.seek(0)
    texto[0] = f"Un texto agregado el: {datetime.now():%Y-%m-%d %H:%M:%S}"
    archivo.writelines(texto)
