import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url=url, timeout=30)
# print(response.status_code)
# print(response.text)
data = response.json()
for user in data:
    # print(user)
    print(f"""
        Nombre: {user['name']}
        Telefono: {user['phone']}
    """)

url = "https://jsonplaceholder.typicode.com/users/9"
response = requests.get(url=url, timeout=30)
data = response.json()
print('===============')
print(data)

# Crear
url = "https://jsonplaceholder.typicode.com/users"
user = {
    # 'id': 11,
    'name': 'Frank Rico',
    'username': 'frico',
    'email': 'frico@dana.io',
    'address': {'street': 'Dayna Park',
                'suite': 'Suite 449',
                'city': 'Bartholomebury',
                'zipcode': '76495-3109',
                'geo': {
                        'lat': '24.6463',
                        'lng': '-168.8889'
                }
                },
    'phone': '(775)976-6794 x41206',
    'website': 'conrad.com',
    'company': {
            'name': 'Yost and Sons',
            'catchPhrase': 'Switchable contextually-based project',
            'bs': 'aggregate real-time technologies'
    }
}
response = requests.post(url=url, timeout=30, data=user)
print(response.status_code)

# Actualizar
url = "https://jsonplaceholder.typicode.com/users/5"
user = {
    'name': 'Frank Rico dev'
}
response = requests.put(url=url, timeout=30, data=user)
print(response.status_code)

# eliminar
url = "https://jsonplaceholder.typicode.com/users/5"
response = requests.delete(url=url, timeout=30)
print(response.status_code)
