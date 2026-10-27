# DJango

```bash
pipenv install django==4.1.7
django-admin startproject nombreProyecto .

python3 manage.py runserver
```

# Crear una app dentro de un proyecto
```
python3 manage.py startapp nombreApp
```

# Cargar los modelos a la base de datos (Migraciones)
```bash
# Es muy importante que en  /NombreProyecto/settings.py se tenga
# vinculado en INSTALLED_APPS la configuración de la nueva app
python3 manage.py makemigrations

# y finalmente ejecutar
python3 manage.py migrate
```
