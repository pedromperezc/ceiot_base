from auth import obtener_token
import requests

url = 'http://localhost:8080/measurement'

headers = {"Content-Type": "application/json; charset=utf-8", "Authorization":"Bearer "+obtener_token()}

data = {"id":"00","t":"30","h":"80"}

response = requests.post(url, headers=headers, json=data)
