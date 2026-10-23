import os
import sys
from pathlib import Path

# python3 /listdata/Documentos/web-dev/python-pato/12-modulos-nativos/05-cli.py -all, holamundo
# > ['/listdata/Documentos/web-dev/python-pato/12-modulos-nativos/05-cli.py', '-all,', 'holamundo']
# print(sys.argv)


def cli(args):
    if len(args) == 1:
        print('No se pasaron argumentos')
        return
    if len(args) != 3:
        print('Se requieren 2 argumentos')
        return

    origen = args[1]
    o = Path(origen)

    if not o.exists():
        print('El origen no existe')
        return

    destino = args[2]
    d = Path(destino)

    if d.exists():
        print('El destino no se le puede dar este nombre:', d)
        return

    if (d.suffix == 'py' or o.suffix == 'py'):
        print('No estas autorizado a modificar este tipo de archivos')
        return

    os.rename(str(origen), str(destino))
    print(f'Archivo renombrado exitosamente «{str(destino)}»')


cli(sys.argv)
