import requests

r = requests.get("http://192.168.60.211:3000")
print(r.text)