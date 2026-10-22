import sqlite3

dbCon = sqlite3.connect('11-sqlite/app.db')
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

# Ejecución de la consulta
dbCon.commit()

dbCon.close()
