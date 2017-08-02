import shutil
import time
import requests
import json


class LoginSession(object):
    __session = None
    information = {"domain": "w.qq.com"}

    def __new__(cls, *args, **kwargs):
        if LoginSession.__session is None:
            LoginSession.__session = object.__new__(cls)
        return cls.__session
            
    def __init__(self):
        self.__session = self.__create_session()
    
    def __create_session(self):
        session = requests.Session()
        session.headers.update(
            {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'})

        QR_code_url = 'https://ssl.ptlogin2.qq.com/ptqrshow?appid=501004106&e=0&l=M&s=5&d=72&v=4&t=0.859513936918227'
        QR_code_response = session.get(QR_code_url, stream=True)
        with open('QR_code.png', 'wb') as out_file:
            shutil.copyfileobj(QR_code_response.raw, out_file)
            print("download QR code success!")
            cookie = QR_code_response.headers["Set-Cookie"]
        del QR_code_response
        qrsig = cookie.split(';')[0].split('=')[1]
        ptqrtoken = self.__translate_qrsig_to_ptqrtoken(qrsig)

        polling_url = 'https://ssl.ptlogin2.qq.com/ptqrlogin?ptqrtoken=' + ptqrtoken + \
            '&webqq_type=10&remember_uin=1&login2qq=1&aid=501004106&u1=http%3A%2F%2Fw.qq.com%2Fproxy.html%3Flogin2qq%3D1%26webqq_type%3D10&ptredirect=0&ptlang=2052&daid=164&from_ui=1&pttype=1&dumy=&fp=loginerroralert&action=0-0-16171&mibao_css=m_webqq&t=undefined&g=1&js_type=0&js_ver=10226&login_sig=&pt_randsalt=0'
        polling_headers = {
            'referer': 'https://ui.ptlogin2.qq.com/cgi-bin/login?daid=164&target=self&style=16&mibao_css=m_webqq&appid=501004106&enable_qlogin=0&no_verifyimg=1&s_url=http%3A%2F%2Fw.qq.com%2Fproxy.html&f_url=loginerroralert&strong_login=1&login_state=10&t=20131024001'
        }
        login_state = False
        while login_state == False:  # start polling
            time.sleep(2)
            polling_response = session.get(polling_url, headers=polling_headers)
            polling_response_result = polling_response.text.split("'")[9]
            print(polling_response_result)
            if polling_response_result == '登录成功！':
                check_sig_url = polling_response.text.split("'")[5]
                login_state = True
                session.get(check_sig_url)  # 虽然返回302，但是设置了一个cookie

        # 从header中取出ptwebqq
        for set_cookie in polling_response.headers["Set-Cookie"].split(','):
            cookie = set_cookie.split(";")[0]
            if 'ptwebqq' in cookie:
                ptwebqq = cookie.split('=')[1].lstrip()
                self.information["ptwebqq"] = ptwebqq
                print("ptwebqq is:", ptwebqq)

        set_cookie_headers = {
            'referer': 'http://w.qq.com/proxy.html?login2qq=1&webqq_type=10'
        }
        set_cookie = session.get(
            "http://web2.qq.com/web2_cookie_proxy.html", headers=set_cookie_headers)

        vfwebqq_url = 'http://s.web2.qq.com/api/getvfwebqq?ptwebqq=' + \
            ptwebqq + '&clientid=53999199&psessionid=&t=1501514974040'
        vfwebqq_header = {
            'Referer': 'http://s.web2.qq.com/proxy.html?v=20130916001&callback=1&id=1'
        }
        vfwebqq_response = session.get(vfwebqq_url, headers=vfwebqq_header)
        vfwebqq_json = json.loads(vfwebqq_response.text)
        vfwebqq = vfwebqq_json["result"]["vfwebqq"]
        self.information["vfwebqq"] = vfwebqq
        print("vfwebqq is :%s" %(vfwebqq))
        return session

    def __translate_qrsig_to_ptqrtoken(self, t):
        e = 0
        i = 0
        n = len(t)
        while n > i:
            e = e + (e << 5) + ord(t[i])
            i = i + 1
        return str(2147483647 & e) 


if __name__ == '__main__':
    a = LoginSession()
    b = LoginSession()
    print(a.information)
    print(b.information)