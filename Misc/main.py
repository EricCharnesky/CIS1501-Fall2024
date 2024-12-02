import requests
import json

response = requests.get("https://api.coincap.io/v2/assets")
#response = requests.get("https://ericcharnesky.github.io/")
print(response.status_code) # 200
print(response.text) # Response content as a string

data = response.json()

for value in data['data']:
    print(value)