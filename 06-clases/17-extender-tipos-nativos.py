# lista = []
"""
lista = list([1, 2, 3])

lista.append(5)
lista.insert(0, 20)

print(lista)  # [20, 1, 2, 3, 5]

"""


class Lista(list):
    def prepend(self, item):
        self.insert(0, item)


lista = Lista([1, 2, 3])
lista.append(5)
lista.prepend(20)
print(lista)  # [20, 1, 2, 3, 5]
