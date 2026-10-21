import csv

import os

# with open("10-archivos/archivo-csv.csv", "w") as archivo:
#    writer = csv.writer(archivo)
#    writer.writerow([
#        'nombre',
#        'Apellido',
#        'edad'
#    ])
#    writer.writerow([
#        'Luis',
#        'Avila',
#        '38'
#    ])
#    writer.writerow([
#        'Maria',
#        'Rivas',
#        '36'
#    ])
#    writer.writerow([
#        'Jesus',
#       'Daza',
#        '40'
#    ])


# with open("10-archivos/archivo-csv.csv") as archivo:
#    reader = csv.reader(archivo)
# print(list(reader))
#    archivo.seek(0)

#    for linea in reader:
#        print(linea)


# Actualizar
with open("10-archivos/archivo-csv.csv", "r") as fLectura, open("10-archivos/archivo-csv-temp.csv", "w") as fEscritura:
    reader = csv.reader(fLectura)
    writer = csv.writer(fEscritura)

    for linea in reader:
        if linea[0] == 'Maria':
            writer.writerow(['Maria', 'Rivas Cardenas', 47])
        else:
            writer.writerow(linea)

    os.remove("10-archivos/archivo-csv.csv")
    os.rename("10-archivos/archivo-csv-temp.csv",
              "10-archivos/archivo-csv.csv")
