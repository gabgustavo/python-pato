from pathlib import Path
from zipfile import ZipFile

# Comprimir archivos
# with ZipFile("10-archivos/mis-comprimidos.zip", "w") as zip:

# el primer * es el nombre del archivo y el segundo la extención
#    for path in Path("10-archivos").rglob('*.*'):
#        print(path)
#        if str(path) != "10-archivos/mis-comprimidos.zip":
#            zip.write(path)


with ZipFile("10-archivos/mis-comprimidos.zip") as zip:
    # print(zip.namelist())
    info = zip.getinfo("10-archivos/06-comprimidos.py")
    print(info.file_size)
    print(info.compress_size)
    zip.extractall("10-archivos/descomprimidos")
