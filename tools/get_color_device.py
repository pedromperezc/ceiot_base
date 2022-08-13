from auth import obtener_token
import requests
import sys

device = sys.argv[1]

url = 'http://localhost:8080/term/device/'+device

headers = {"Content-Type": "application/json; charset=utf-8",
                   "Authorization":"Bearer "+obtener_token()}

response = requests.get(url, headers=headers)

print(response.text)
