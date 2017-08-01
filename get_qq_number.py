import requests

url = "http://s.web2.qq.com/api/get_friend_uin2?tuid=\#{uin}&type=1&vfwebqq=\#{vfwebqq}&t=0.1"
headers = {
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'Content-Type': 'utf-8',
    'Accept': '*/*',
    'Referer': 'http://cgi.connect.qq.com/proxy.html?t=20120217001&callback=1&id=1',
    'Cookie': 'tvfe_boss_uuid=7076168915e28690; pac_uid=1_827167063; sd_userid=83141472573372919; sd_cookie_crttime=1472573372919; _gscu_661903259=73503010btvdoi11; RK=aW1q48bLV1; eas_sid=11x580y0D5H5L2j7K235r724s6; LW_uid=71P5G0Z0W5D5K2m7h3l3q1H1U7; ue_ts=1500643435; ue_uk=1d31a720269d36cfc94994456f2be965; ue_uid=dcdf6cde3d677601819afbc892c591d2; ue_skey=45e152b27d4cc1f76fc461ceaed9f145; pgv_pvi=9027965952; LOL_a20160921hextech_bind_827167063=8; LW_sid=y1X540y1m2p4w4L30097b6K8W7; pgv_si=s687044608; ptui_loginuin=1827820113@qq.com; _qpsvr_localtk=0.011473223308861025; rv2=80FCB18E91CF95ED90B0B795D139C85268BE33BE590C0618CE; property20=FB1E5B5C0162408FEFFD81D61DD682B09C6E59644117A2B15FB7932A4DC31C169B1B51500D8E1E27; o_cookie=827167063; IED_LOG_INFO2=userUin%3D827167063%26nickName%3D%2525E8%2525B6%252585%2525E9%2525AB%252598%2525E6%2525A0%2525A1%2525E7%2525BA%2525A7%2525E7%25259A%252584%2525E5%2525B0%25258F%2525E4%2525B8%252591%26userLoginTime%3D1501406273; qv_swfrfh=www.loldk.com; qv_swfrfc=v20; qv_swfrfu=http://www.loldk.com/fm/f/a/aviewclient-9834.html; ptisp=ctc; ptcz=6e1982086429e4c83cc4774fab2b9a7d11de50a418cf2ddef45c6560c0d239c9; pgv_info=ssid=s8511824686&pgvReferrer=; pgv_pvid=9471847140; pt2gguin=o0827167063; uin=o0827167063; skey=@eLjePyZT0; p_uin=o0827167063; p_skey=4RvO2sJQMxKWgJK3glYOOMqvhq4QkoKp9lvjYK6wOn8_; pt4_token=eF5KE4qO6Ha1aofiCTOTE2aA-tVh8B5jR43XtzECfeQ_; verifysession=h0135d5d93474844c79b14d1a812d6ff405bbb1e0c0d2e51e5add2442ab165946a3542cd2d447ef34f5; visibleShare=0,0; ui=BB0CFAB0-6968-4C16-B80F-5208A0622F70',
    'Connection': 'keep-alive'
}

r = requests.get(url, headers=headers)

fo = open("qq_number.json", "wb")
fo.write(r.text.encode("utf-8"))
fo.close()
