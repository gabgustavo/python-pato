animanl = "  elefante   Elegante "
print(animanl.upper())  # Convierte a mayusculas
print(animanl.lower())  # convierte a minusculas
# convertir la primera letra en mayuscula y elimina espacios al inicio y final
# convertir la primera letra en mayuscula y elimina espacios al inicio y final
print(animanl.strip().capitalize())
print(animanl.title())  # convirte la primera letra de cada palabra en mayuscula
print(animanl.strip())  # elimina espacios al inicio y final
print(animanl.lstrip())  # elimina espacios al inicio
print(animanl.rstrip())  # elimina espacios al final
print(animanl.find('an'))  # busca la posicion de la primera ocurrencia de 'an'
# busca la posicion de la primera ocurrencia de 'asd'
print(animanl.find('asd'))
print(animanl.replace('elefante', 'leon'))  # reemplaza 'elefante' con 'leon'
print('ante' in animanl)
print('ante' not in animanl)
