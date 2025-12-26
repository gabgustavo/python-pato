def noSpace(string):
    nuevoString = ''
    for char in string:
        if char != ' ':
            nuevoString += char
    return nuevoString


def reverseString(string):
    """
    Esta función recibe un string y devuelve el string invertido.
    """
    reversed_str = ''
    for char in string:
        reversed_str = char + reversed_str
    return reversed_str


def isPalindromo(string):
    """
    Esta función recibe un string y devuelve True si es un palíndromo
    (se lee igual de izquierda a derecha que de derecha a izquierda) 
    y False en caso contrario.
    """
    # Eliminar espacios y convertir a minúsculas para una comparación precisa
    # cleaned_string = ''.join(string.split()).lower()
    cleaned_string = noSpace(string).lower()
    # reversed_string = cleaned_string[::-1]
    reversed_string = reverseString(cleaned_string)
    print(f" inicial: {cleaned_string}\n final: {reversed_string}")
    # Comparar el string con su reverso
    return cleaned_string == reversed_string


texto = "Amor a Roma"
print(isPalindromo(texto))

texto = "Hola Mundo"
print(isPalindromo(texto))
