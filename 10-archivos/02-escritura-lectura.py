from pathlib import Path

archivo = Path("10-archivos/archivo-prueba.txt")
texto = archivo.read_text()
# print(texto)

texto = archivo.read_text('utf-8').split('\n')
print(texto)

texto.insert(0, 'Esta es una escriptura de prueba')
archivo.write_text('\n'.join(texto), 'utf-8')
