from pathlib import Path

path = Path('directorio')

# path.exists()  # => False, no existe el directorio
# path.mkdir()  # => crea el directorio, si no existe
# path.rmdir()  # => elimina el directorio, si existe y esta vacio
# path.rename('directorio-renombrado')  # => renombra el directorio, si existe

# => devuelve un iterador con los archivos y carpetas dentro del directorio, si existe
print(path.iterdir())

archivos = [p for p in path.iterdir() if p.is_file()]
archivos = [p for p in path.iterdir() if not p.is_file()]
# => devuelve un iterador con los archivos que cumplen con el patron, si existe
archivos = [p for p in path.glob('*.txt')]
# => busca en subdirectorios tambien, si existe
archivos = [p for p in path.glob('**/*.txt')]
# recursivo, busca en subdirectorios tambien
archivos = [p for p in path.rglob('**/*.txt')]
print(archivos)
