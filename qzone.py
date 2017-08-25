import requests
from login import LoginSession

session = LoginSession()
response = session.session.get("https://user.qzone.qq.com/827167063")
f = open("qzone", "wb")
num = f.write(response.text.encode("utf-8"))
f.close()