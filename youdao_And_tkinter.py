import requests,os
import time
import hashlib
from Crypto.Cipher import AES #解密AES
import base64 #由于抓包得到了密文被编码成了base64，所以要导入这个包进行改变编码方式
from Crypto.Util.Padding import unpad #清除生成AES解密以后的填充区域
import re
import tkinter as tk
from tkinter import messagebox
from settings import *

#打包形成可执行为文件
#pyinstaller -F -w -i      t.ico          youdao_And_tkinter.py
#-F （= --onefile）参数代表生成单一exe文件，-D (= --onedie)生成一个目录
#-w  (= --windowed,--nocomsole)运行时不出现命令窗口，   -c  (= --console,--nocomsole)出现窗口（不不写-w就默认为-c）
#-i (= --icon)给应用程序添加图标（以.ico为后缀，大小32x32）,后面接上图标的路径
#要打包的文件.py路径在最后写

os.system("cls")
class GUi:

    def __init__(self):
        self.root=tk.Tk()
        self.root.title("Translate")
        self.root.resizable(False,False)#是否能改变窗口的高和宽
        #self.root.iconbitmap(".ico")#设置窗口图标，需要指定图标文件（.ico）
        #root.config(bg="")改变窗口背景色
        self.root.geometry("450x300+1000+200")
        self.interface()

    def interface(self):
        self.label1=tk.Label(self.root,text="   language1                   ------>              language2",fg="black")
        self.label1.place(relx=0.05,rely=0.05,relwidth=0.8,relheight=0.05)

        self.entry1=tk.Entry(self.root)
        self.entry1.place(relx=0.1,rely=0.1,relwidth=0.3,relheight=0.1)
        self.entry2=tk.Entry(self.root)
        self.entry2.place(relx=0.6,rely=0.1,relwidth=0.3,relheight=0.1)

        self.btn1=tk.Button(self.root,text="确认",command=self.btn1_language)#确认语言的按键,command参数将绑定执行的事件
        self.btn1.place(relx=0.45,rely=0.12,relwidth=0.1,relheight=0.08)
        self.btn4=tk.Button(self.root,text="语言",command=self.btn4_language)
        self.btn4.place(relx=0.9,rely=0.10,relheight=0.05,relwidth=0.08)
        self.btn5=tk.Button(self.root,text="交换",command=self.btn5_change)
        self.btn5.place(relx=0.9,rely=0.15,relheight=0.05,relwidth=0.08)
       

        self.label2=tk.Label(self.root,text="要翻译的文本：")
        self.label2.place(relx=0.1,rely=0.25,relheight=0.05)

        self.text1=tk.Text(self.root)
        self.text1.place(relx=0.1,rely=0.3,relheight=0.2,relwidth=0.8)

        self.btn2=tk.Button(self.root,text="翻译",command=self.btn2_translate)#翻译的按键
        self.btn2.place(relx=0.2,rely=0.52,relheight=0.08,relwidth=0.1)

        self.btn3=tk.Button(self.root,text="清空",command=self.btn3_clear)
        self.btn3.place(relx=0.7,rely=0.52,relheight=0.08,relwidth=0.1)

        self.text2=tk.Text(self.root)
        self.text2.place(relx=0.1,rely=0.62,relheight=0.23,relwidth=0.8)

    def btn1_language(self):#第一个确认按钮的函数,返回一个translator对象，语言转换
        from_lang=self.entry1.get()
        to_lang=self.entry2.get()
        return [from_lang,to_lang]
        

    def btn2_translate(self):#翻译
        from_lang,to_lang=self.btn1_language()
        text_to_be_translated=self.text1.get(0.0,"end")
        if text_to_be_translated!="\n":   
            data=self.get_data(from_lang,to_lang,text_to_be_translated)
            ciphertext=self.send_request(data)
            text=self.get_translation(ciphertext)
    
            self.text2.insert(0.0,text[0])#将文本框的文本翻译好后的文本插入文本框2,第一个参数为插入的位置,第二个为插入的字符串
        else:
            messagebox.showerror(title="错误",message="请输入要翻译的内容")
    def btn3_clear(self):#清空输入翻译和输出翻译的文本框
        self.text1.delete(1.0,"end")
        self.text2.delete(1.0,"end")

    def btn4_language(self):
        language_string=self.get_langguage()
        messagebox.showinfo(title="各国语言缩写",message=language_string)

    def btn5_change(self):
        from_lang,to_lang=self.btn1_language()

        self.entry1.delete(0,"end")
        self.entry2.delete(0,"end")

        self.entry1.insert(0,to_lang)
        self.entry2.insert(0,from_lang)
    

    def get_langguage(self):#不同语言的缩写
        with open("language.txt","a") as fp:
            pass
        if os.path.getsize("language.txt")==0:
            url="https://api-overmind.youdao.com/openapi/get/luna/dict/luna-front/prod/langType"
            headers={
                'Referer': 'https://fanyi.youdao.com/',
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0",
                "Cookie" :Cookie,
            }


            response=requests.get(url=url,headers=headers)
            response.raise_for_status()
            response.encoding=response.apparent_encoding

            string=str(response.json())
            regexes=re.compile(r"'code': '(.*?)', 'label': '(.*?)'")

            dictionay_list=regexes.findall(string)
            print(len(dictionay_list))#得到不同语言编号的缩写

            with open("language.txt","w",encoding="utf-8") as fp:
                fp.write("各国的语言的缩写(英文缩写和语言)：\n")
                c=0
                for i in dictionay_list:
                    fp.write(f'     {i[0]}  --{i[1]}')
                    if c==3:
                        fp.write("\n")
                        c=0
                    else :
                        c+=1
        with open("language.txt","r",encoding="utf-8") as fp:
            language_string=fp.read()
        return language_string                        



    def get_Time_Sign(self):#获取加密后的sign（构造加密函数）
        mysticTime=int(time.time()*1000)

        # key=Vy4EQ1uwPkUoqvcP1nIu6WiAjxFeA3Y9 中的key也是在https://dict.youdao.com/webtranslate/key?keyid=webfanyi-key-getter&sign=7de12753d8e473c6f0068a28ea73c630&client=fanyideskweb&product=webfanyi&appVersion=1.0.0&vendor=web&pointParam=client,mysticTime,product&mysticTime=1736665826733&keyfrom=fanyi.web&mid=1&screen=1&model=1&network=wifi&abtest=0&yduuid=abcdefg
        # 的secretKey,是会改变的

        string=f"client=fanyideskweb&mysticTime={mysticTime}&product=webfanyi&key={SecretKey}"  #sign加密前的字符串()#fsdsogkndfokasodnaso要抓包得到，有两个值，选择第二个（第一个为asdjnjfenknafdfsdfsd#第一个url的sign的key=），也可以在第一个url中获得“"https://dict.youdao.com/webtranslate/key?keyid=webfanyi-key-getter&sign=823beceb3a00c3cd2e42323fda20056c&client=fanyideskweb&product=webfanyi&appVersion=1.0.0&vendor=web&pointParam=client,mysticTime,product&mysticTime=1730355400284&keyfrom=fanyi.web&mid=1&screen=1&model=1&network=wifi&abtest=0&yduuid=abcdefg”"
        MD5=hashlib.md5()
        MD5.update(string.encode())#使用hash时要将字符串的编码改为bytes类型
        sign=MD5.hexdigest()
        return [mysticTime,sign]  



    def get_data(self,from_lang,to_lang,text_to_be_translated):#得到发送post的data数据
        mysticTime,sign=self.get_Time_Sign()
        data={
            "i": text_to_be_translated,
            "from": from_lang,
            "to": to_lang,
            "useTerm": "false",
            #"domain": "0",
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
                         
    def send_request(self,data):#
        url="https://dict.youdao.com/webtranslate"
        headers={
            'Referer': 'https://fanyi.youdao.com/',
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0",
            "Cookie":Cookie,
        }

        response=requests.post(url=url,headers=headers,data=data)
        response.encoding=response.apparent_encoding
        response.raise_for_status()

        return response.text#这个就是有道翻译发给我们的翻译结果，但是是密文，需要解密                            

    def get_translation(self,ciphertext):#解密得到的response.text的密文：转化为明文。（利用到了AES加密的CBC模式，存在密钥key，和偏移量Iv）

        Key="ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl".encode()#编码为bytes类型
        Iv= "ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4".encode()#因为使用的是经过md5加密后的key和iv，所以要先加密key和iv(抓包得到其加密为二进制数据，所以用digest（），而不是hexdigest（）)

        key_md5=hashlib.md5((Key)).digest()#AES加密的密钥
        iv_md5=hashlib.md5((Iv)).digest()#AES加密的偏移量（只有CBC模式才有iv）

        cipher=AES.new(key=key_md5,mode=AES.MODE_CBC,iv=iv_md5)#创建AES解密对象
        ciphertext=base64.urlsafe_b64decode(ciphertext)#对密文为bytes类进行编码为base64类，由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_：



        text_dictionary=unpad(cipher.decrypt(ciphertext),AES.block_size)#cipher.decrypt()为AES对象的解密函数，AES加密时通常会对明文进行填充，以确保其长度是块大小的整数倍。解密后需要去除填充。
                                                                            #unpad（）是一个Crypto.Util.Padding中的函数，用于去除填充，AES.block_size是AES的块大小（通常是16字节）
        text_dictionary=text_dictionary.decode()#解码
        print(text_dictionary)
        textRegexes=re.compile(r'translateResult.*"tgt":"(.*)","src":"(.*)",')#提取明文中的翻译部分，tgt对应下的为翻译结果，src为要翻译的内容

 

        text_translation_list=textRegexes.findall(text_dictionary)
        if text_translation_list==[]:
            print("翻译失败")
            quit()
        for i in text_translation_list:
            text_list=list(i)
            break
        return text_list          

                             



if __name__=="__main__":
    a=GUi()
    a.root.mainloop()



