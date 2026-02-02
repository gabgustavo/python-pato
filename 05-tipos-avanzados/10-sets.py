# set seria grupo o conjunto
# el set no se puede repetir ni esta ordenada ni acceder a un elemento

primero = {1, 1, 2, 2, 3, 3, 4, 4, 5}
print(primero)

primero.add(6)
primero.remove(3)

print('-' * 30)
segundo = [5, 6, 7, 8]
segundo = set(segundo)
print(segundo)

# union
print(primero | segundo)
# intersección retorna los "numeros" en comun
print(primero & segundo)
# diferencia
print(primero - segundo)
# diferencia simétrica
print(primero ^ segundo)

# se puede validar
if 8 in segundo:
    print('El dato se encontro')
