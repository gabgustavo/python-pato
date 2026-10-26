import requests
from bs4 import BeautifulSoup


url = 'https://cursosdev.com/coupons'

response = requests.get(url=url, timeout=30)
texto = response.text

print(texto)
soup = BeautifulSoup(texto, 'html.parser')

cursos = soup.select(
    '.group.relative.h-full')
print(cursos[0])

for curso in cursos:
    titulo = curso.select_one('.mt-2.font-bold.text-gray-900').get_text()
    idioma = curso.select_one(
        '.px-4.py-3.border-t.border-gray-200 span').get_text()

    print(f"Curso: {titulo} en {idioma}")
