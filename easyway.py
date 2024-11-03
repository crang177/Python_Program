import requests
url="http://172.30.21.100/api/account/login"
data={
    "username": "",
    "password": "",
    "switchip": "",
    "nasId": "52",
    "userIpv4": "",
    "userMac": "",
    "captcha": '',
    "captchaId": '' ,
}
headers={
    "Referer": "http://172.30.21.100/tpl/whut/login.html?acip=172.30.1.223&acname=WHUT-Bras-ME60-A&ip=10.84.131.112&nasId=52&userip=10.84.131.112&wlanacname=",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"
}
res=requests.post(url=url,headers=headers,data=data)
if res.status_code==200:
    print("登录成功")
else :
    print("安装失败")