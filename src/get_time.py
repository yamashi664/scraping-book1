import requests

#時刻を提供しているサーバにアクセス
url = 'https://api.aoikujira.com/time/get.php'
result = requests.get(url)

#アクセス結果
print("ok=", result.ok)

if result.ok:
    print("text=",result.text)

#ステータスコードの確認    
print("status_code=",result.status_code)
