import requests

url = "https://example.com/login"
data = {"username": "fukura", "password": "1234"}
res = requests.post(url, data=data)

print(res.status_code)
print(res.text[:500])

