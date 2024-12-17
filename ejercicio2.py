import requests

r = requests.patch("http://192.168.60.211:3000/metodo")
print(r.text)