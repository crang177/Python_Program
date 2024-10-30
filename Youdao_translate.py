import tkinter as tk
import requests,os
import time
import hashlib
from Crypto.Cipher import AES #解密AES
import base64 #由于抓包得到了密文被编码成了base64，所以要导入这个包进行改变编码方式
from Crypto.Util.Padding import unpad #清除生成AES解密以后的填充区域
import re


def get_Time_Sign():#获取加密后的sign（构造加密函数）
    mysticTime=int(time.time()*1000)
    string=f"client=fanyideskweb&mysticTime={mysticTime}&product=webfanyi&key=fsdsogkndfokasodnaso"  #sign加密前的字符串()

    MD5=hashlib.md5()
    MD5.update(string.encode())#使用hash时要将字符串的编码改为bytes类型
    sign=MD5.hexdigest()
    return [mysticTime,sign]


def get_data():#得到发送post的data数据
    mysticTime,sign=get_Time_Sign()
    text_to_be_translated=input("输入要翻译的文本：")
    data={
    "i": text_to_be_translated,
    "from": "zh-CHS",
    "to": "en",
    "useTerm": "false",
    "domain": "0",
    "dictResult": "true",
    "keyid": "webfanyi",
    "sign": sign,
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
    return data

def send_request(data):
    url="https://dict.youdao.com/webtranslate"
    headers={
        'Referer': 'https://fanyi.youdao.com/',
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0",
        "Cookie":"OUTFOX_SEARCH_USER_ID=-500824836@113.57.237.83; OUTFOX_SEARCH_USER_ID_NCOO=1469770841.1152; DICT_DOCTRANS_SESSION_ID=NjY0NzdjZDktYmQ1ZS00ZWQ2LTljOWMtZTc2NmFlMzk4Y2Uw; _uetsid=c7c7e880945911efa2836922858ec728; _uetvid=93f31c607d7a11ef8214cf73d83f3357",

    }

    response=requests.post(url=url,headers=headers,data=data)
    response.encoding=response.apparent_encoding
    response.raise_for_status()

    return response.text#这个就是有道翻译发给我们的翻译结果，但是是密文，需要解密

def get_translation(ciphertext):#解密得到的response.text的密文：转化为明文。（利用到了AES加密的CBC模式，存在密钥key，和偏移量Iv）

    Key="ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl".encode()#编码为bytes类型
    Iv= "ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4".encode()#因为使用的是经过md5加密后的key和iv，所以要先加密key和iv(抓包得到其加密为二进制数据，所以用digest（），而不是hexdigest（）)

    key_md5=hashlib.md5((Key)).digest()#AES加密的密钥
    iv_md5=hashlib.md5((Iv)).digest()#AES加密的偏移量（只有CBC模式才有iv）

    cipher=AES.new(key=key_md5,mode=AES.MODE_CBC,iv=iv_md5)#创建AES解密对象
    ciphertext=base64.urlsafe_b64decode(ciphertext)

    text_dictionary=unpad(cipher.decrypt(ciphertext),AES.block_size)
    text_dictionary=text_dictionary.decode()#解码

    textRegexes=re.compile(r'"translateResult":[[{"tgt":"(.*)","src":"(.*)",')
    text_translation_list=textRegexes.findall(text_dictionary)
    if text_translation_list==[]:
        print("翻译失败")
        quit()
    text=text_translation_list[0]
    return text



if __name__=="__main__":
    data=get_data()
    ciphertext=send_request(data)
    text=get_translation(ciphertext)
    print(text)











#asdjnjfenknafdfsdfsd#第一个url的sign的key=


"""{
    "data": {
        "secretKey": "fsdsogkndfokasodnaso",
        "aesKey": "ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl",
        "aesIv": "ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4"
    },
    "code": 0,
    "msg": "OK"
}"""

# os.system("cls")
# a="ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl".encode("utf-8")
# md5=hashlib.md5()
# md5.update(a)
# b=md5.digest()
# print(list(b))#写成列表形式得到，每个元素都是一个字节值（0-255之间的整数）。运行这段代码后， b_list  将包含 MD5 哈希值的每个字节。