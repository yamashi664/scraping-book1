import requests
import os, time

#取得した画像ファイルの保存先
base_dir = os.path.dirname(os.path.abspath(__file__))
save_dir = os.path.abspath(os.path.join(base_dir, "..", "data", "image2"))

def download_all():
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    
    for id in range(1,11):
        download_file(id)
        time.sleep(1)        

def download_file(id):
    url = f"https://uta.pw/shodou/img/{id%31}/{id}.png"
    res = requests.get(url)

    if not res.ok :
        print("失敗です。status_code:", res.status_code)
        return()
    
    save_file = save_dir + '/' + str(id) + '.png'
    with open(save_file, 'wb') as fp:
        fp.write(res.content)
    print("save:", save_file)




if __name__ == '__main__':
    download_all()