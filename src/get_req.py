import requests

url = "https://example.com/search"
params = {"q":"python", "lang":"ja"}
res = requests.get(url, params=params)
print(res.url)
print(res.text[:500])
