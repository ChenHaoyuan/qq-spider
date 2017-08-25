import requests
from login import *

login_session = LoginSession()

url = "http://cgi.connect.qq.com/qqconnectopen/openapi/get_user_friends?t=150160210484"
headers = {
    'Referer': 'http://cgi.connect.qq.com/proxy.html?t=20120217001&callback=1&id=1'
}

r = login_session.session.get(url, headers=headers)

print(r.text)
print(login_session.session.cookies)
fo = open("friends_uin.json", "wb")
fo.write(r.text.encode("utf-8"))
fo.close()