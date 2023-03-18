from fastapi import requests
import requests
import base64

url = "https://oss.jetlab.live/api/upload/"

def upload(file):
    file = base64.b64decode(file)
    with open("temp.jpg", "wb") as f:
        f.write(file)
    files = {'files': open('temp.jpg', 'rb')}
    r = requests.post(url, files=files, verify=False)
    if r.status_code == 200:
        return r.json()
    else:
        return "Error"


# 读取 1.jpg 图片, 转为 base64 编码, 上传到 API
# with open("../1.jpg", "rb") as f:
#     file = base64.b64encode(f.read())
#     print(upload(file))
