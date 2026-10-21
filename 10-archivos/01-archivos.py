from pathlib import Path
from time import ctime

archivo = Path("10-archivos/archivo-prueba.txt")
# archivo.exists()
# archivo.rename()
# archivo.unlink()

# print(archivo.stat())
print('Acceso ', ctime(archivo.stat().st_atime))
print('Creación ', ctime(archivo.stat().st_ctime))
print('Modificación ', ctime(archivo.stat().st_mtime))
