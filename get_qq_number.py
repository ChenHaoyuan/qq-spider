import requests
from login import * 

login_session = LoginSession()
login_session.information

uin = '3043699056'
url = 'http://s.web2.qq.com/api/get_friend_info2?tuin=' + uin + '&type=1&vfwebqq='+ login_session.information['vfwebqq'] +'&t=0.1'
headers = {
    'referer': 'http://d1.web2.qq.com/proxy.html?v=20151105001&callback=1&id=2'
}
r = login_session.session.get(url, headers=headers)
print(r.text)