# python-pato

## Entornos virtuales

### Crear un entorno nuevo
```bash

python3 -m venv venv
source venv/bin/activate

python3 -m venv nombreDeMiEntorno
```

### Activar el entorno virtual

```bash

source venv/bin/activate
```

### Desactivar el entorno virtual
```bash

deactivate
```

## PIP
```bash
# Paquetes https://pypi.org/

pip list

# pip install pipenv

# desinstalar un paquete
pip uninstall nombrePaquete

# instalar una version en especifico de un paquete
pip uninstall requests==2.18.1
pip uninstall requests==2.18.*
pip uninstall requests==~2.18.1 # se instala la mejor version 
```

# VARIABLES DE ENTORNO
en el archivo .env
```python
NOMBRE_DE_VARIABLE = "Su valor corespondiente"

# en su archivo a usar:
import os

miVariable = os.environ.get('NOMBRE_DE_VARIABLE')

from dotenv import load_dotenv

load_dotenv()

apiKey = os.getenv('NOMBRE_DE_VARIABLE')
```