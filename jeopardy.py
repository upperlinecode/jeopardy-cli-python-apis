import requests

response = requests.get('http://jservice.io/api/clues?category=139').json()

print(response)