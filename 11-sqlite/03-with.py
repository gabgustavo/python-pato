import sqlite3

# with abre y cierra la conexión, al cerrar llama __exit__
# y este llama a close y antes de cerrar llama a commit
with sqlite3.connect('11-sqlite/app.db') as dbCon:
    # cursor es un intermediario entre sqlite y nosotros para hacer consultas
    cursor = dbCon.cursor()
    # Crear tablas

    # Preparación de la consulta
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS usuarios(
                id INTEGER primary key,
                nombre VARCHAR(50)
            );
        """
    )
