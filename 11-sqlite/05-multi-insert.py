import sqlite3

# with abre y cierra la conexión, al cerrar llama __exit__
# y este llama a close y antes de cerrar llama a commit
with sqlite3.connect('11-sqlite/app.db') as dbCon:
    # cursor es un intermediario entre sqlite y nosotros para hacer consultas
    cursor = dbCon.cursor()
    # Preparación de la consulta
    usuarios = [
        (2, "Maria"),
        (3, "Carlos"),
        (4, "Juan"),
        (5, "Mateo"),
        (6, "Felipe"),
        (7, "Frank"),
    ]
    cursor.executemany(
        "INSERT INTO usuarios VALUES(?, ?);",
        usuarios,
    )
