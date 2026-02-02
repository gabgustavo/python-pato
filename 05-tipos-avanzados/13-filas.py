from collections import deque
# FIFO
# first int, first out...

# al hacer el movimiento de elementos esto puede ser muy pesado para la maquina
lista = [2,  4]

fila = deque([7, 8, 9])
fila.append(10)
fila.append(11)

print(fila)
fila.popleft()
fila.popleft()
fila.popleft()
fila.popleft()
fila.popleft()
print(fila)

# validar si es que ya esta la fila vacia
if not fila:
    print('No hay nadie que atender')
