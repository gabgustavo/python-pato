usuarios = [["Juan", 25],
            ["Ana", 30],
            ["Pedro", 20],
            ["María", 27]
            ]
nombres = []
for user in usuarios:
    nombres.append(user[0])

print(nombres)
print('-' * 20, 'map')

# en otros entornos son conocidas como MAP
nombres = []
# nombres = [expresion for user in usuarios]
nombres = [user[0] for user in usuarios]
print(nombres)

print('-' * 20, 'filter')
# filtrar /  filter
nombres = []
nombres = [user for user in usuarios if user[1] > 25]
print(nombres)

print('-' * 20, 'filtrar y transformar')
# filtrar y transformar // en este otro seria 2 pasos x separado
nombres = []
nombres = [user[0] for user in usuarios if user[1] > 25]
print(nombres)

print('-' * 20, 'list > lambda')
nombres = []
nombres = list(map(lambda user: user[0], usuarios))
print(nombres)

print('-' * 20, 'list > filter lambda')
nombres = []
nombres = list(filter(lambda user: user[1] > 27, usuarios))
print(nombres)
