
n1 = input("Ingrese un primer número: ")
n1 = int(n1)
n2 = input("Ingrese un segundo número: ")
n2 = int(n2)

suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
divi = n1 / n2

mensaje = f"""
 { n1 } + { n2 } = {suma}
 { n1 } - { n2 } = {resta}
 { n1 } x { n2 } = {multi}
 { n1 } / { n2 } = {divi}
"""

print(mensaje)
