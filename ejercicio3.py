import requests
url = 'http://192.168.60.211:3000/shared_data'
data = {'data': 'valor'}
r = requests.post(url,params=data)

print(r.text)
r = requests.post(url,data=data)
print(r.text)
