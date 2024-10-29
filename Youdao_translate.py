import tkinter as tk
import requests,os
import time
import hashlib


url="https://fanyi.youdao.com/#/TextTranslate"
headers={
   "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0",

}



mysticTime=int(time.time()*1000)
print(mysticTime)
#client=fanyideskweb&mysticTime={time}&product=webfanyi&key=fsdsogkndfokasodnaso  sign加密前的字符串
#asdjnjfenknafdfsdfsd#第一个url的sign的key=
data={
   "i": "你好",
   "from": "zh-CHS",
   "to": "en",
   "useTerm": "false",
   "domain": "0",
   "dictResult": "true",
   "keyid": "webfanyi",
   "sign": "",
   "client": "fanyideskweb",
   "product": "webfanyi",
   "appVersion": "1.0.0",
   "vendor": "web",
   "pointParam": "client,mysticTime,product",
   "mysticTime": f"{mysticTime}",
   "keyfrom": "fanyi.web",
   "mid": "1",
   "screen": "1",
   "model": "1",
   "network": "wifi",
   "abtest": "0",
   "yduuid": "abcdefg",
}

"""{
    "data": {
        "secretKey": "fsdsogkndfokasodnaso",
        "aesKey": "ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl",
        "aesIv": "ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4"
    },
    "code": 0,
    "msg": "OK"
}"""