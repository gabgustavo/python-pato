from pathlib import Path

# para windows, permite usar la barra invertida, pero hay que poner una r antes de la cadena para que no se interpreten los caracteres de escape
# Path(r"C:\Users\Usuario\Documents\web-dev\python-pato\09-rutas")

# esto crea una ruta para ese directorio, esta es una ruta absoluta
# Path('/usr/bin')

# Esta es una ruta dependiendo de donde nos encontremos
# Path()

# Crear una ruta al home del usuario
# Path.home()

# tambien a un archivo, pero esta es una ruta relativa
# Path('09-rutas/01-path.py')

# el archivo / carpeta no es necesario que exista, solo es una ruta
path = Path('mi-carpeta/mi-archivo.py')
# path = Path('./08-modulos/app.py')
# para saber si es un archivo
print(path.is_file())

# para saber si es un directorio
print(path.is_dir())

# para saber si existe
print(path.exists())

print("::>",
      f"name: {path.name}\n",  # nombre del archivo
      f"stem: {path.stem}\n",  # nombre del archivo sin extension
      f"suffix: {path.suffix}\n",  # extension del archivo
      f"parent: {path.parent}\n",  # carpeta padre
      f"absolute: {path.absolute()}"  # ruta absoluta
      )

# cambia el nombre del archivo, pero mantiene la ruta
p = path.with_name('mi-archivo-2.py')
print(p)

# cambia la extension del archivo, pero mantiene la ruta
p = path.with_suffix('.txt')
print(p)

# cambia el nombre del archivo, pero mantiene la ruta
p = path.with_stem('siiiii')
print(p)
