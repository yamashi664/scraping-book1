import requests
import os

#画像ファイルのURL
url = 'https://uta.pw/shodou/img/3/3.png'

res = requests.get(url)

#戻り値チェック
if not res.ok :
    print("失敗です。status_code:", res.status_code)
    quit()

#取得した画像ファイルの保存先
base_dir = os.path.dirname(os.path.abspath(__file__))
save_dir = os.path.abspath(os.path.join(base_dir, "..", "data", "image1"))
file_path = os.path.join(save_dir, "gyudon.png")

#ファイルに保存
with open(file_path, 'wb') as fp:
    fp.write(res.content)
print("ok.")