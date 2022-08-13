from auth import obtener_token
import requests
import sys

id = sys.argv[1]
name = sys.argv[2]
key = sys.argv[2]

url = 'http://ec2-3-92-88-175.compute-1.amazonaws.com:8080/device'

data = {"id":id,"n":name,"k":key}

headers = {"Content-Type": "application/json; charset=utf-8",
                   "Authorization":"Bearer "+obtener_token()}

response = requests.post(url, headers=headers, json=data)
