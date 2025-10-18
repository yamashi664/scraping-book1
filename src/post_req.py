import requests

url = "https://example.com/login"
data = {"username": "sample", "password": "1122"}
res = requests.post(url, data=data)

print(res.status_code)
print(res.text[:500])

