import requests

url = "https://jsonplaceholder.typicode.com/users/5"
apyKey = "My-api_key"
headers = {
    "Authorization": f"Bearer {apyKey}"
}

response = requests.delete(url=url, timeout=30, headers=headers)
print(response)
