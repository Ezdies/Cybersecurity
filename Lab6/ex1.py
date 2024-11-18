import requests

headers = {} #to jest mapa, więc robimy jako klucz i wartość
response = requests.get("http://", headers=headers)
print(response.text)