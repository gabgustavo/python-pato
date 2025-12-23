# and, or, not

gas = True
encendido = True
edad = 18

print('_' * 20, 'AND')
if gas and encendido:
    print("El auto está en marcha")
else:
    print("El auto está detenido")

print('_' * 20, 'OR')
if gas or encendido:
    print("El auto está en marcha")
else:
    print("El auto está detenido por algun evento")

print('_' * 20, 'NOT')
if not gas or encendido:
    print("Avanzando")
else:
    print("No se puede avanzar")

print('_' * 20, 'and multiple')
if gas and encendido and edad > 17:
    print("Avanzar")
else:
    print("No se puede avanzar, no cumple con las condiciones")


print('_' * 20, 'and or combined')
if gas and (encendido or edad > 17):
    print("Avanzar...")
else:
    print("No se puede avanzar, no cumple con las condiciones")

print('_' * 20, 'not, and or combined')
if not gas and (encendido or edad > 17):
    print("Avanzar *")
else:
    print("No se puede avanzar, no cumple con las condiciones *")


print('_' * 20, 'and de corto circuito, si una condicion es falsa no evalua las demas')
if not gas and encendido and edad > 17:
    print("Avanzar ***")
else:
    print("No se puede avanzar, no cumple con las condiciones ***")
