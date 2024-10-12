from selenium import webdriver 
from selenium.webdriver.common.by import By
import time,os,json,os.path
import pyinputplus as pyip
from pathlib import Path
from ansilib import ansi
import hashlib
import shelve


os.system("cls")


def user_name_password():#输入账号密码
    user_id=pyip.inputInt(prompt="请输入你的用户名：")
    user_password=pyip.inputStr(prompt="请输入你的密  码：")
    user_massage=[user_id,user_password]
    return user_massage

def password_hexdigest(Password):#md5加密
    md5=hashlib.md5()#创建md5对象
    Password_user=Password.encode(encoding="utf-8")#格式转化
    md5.update(Password_user)#给入加密参数
    userPassword=md5.hexdigest()#加密
    password=[Password,userPassword]
    return password

def save_password(password):#保存原来真实的密码（二进制）
    shelffile=shelve.open("mm")
    shelffile["password"]=password
    shelffile.close()


def read_password():#读取原来真实的密码
    shelffile=shelve.open("mm")
    password=shelffile["password"]
    shelffile.close()
    return password


def user_exist():#判断账号是否存在
    with open("user.json","a",encoding="utf-8"):
        path=Path("user.json")
        pass
    if os.path.getsize(path)==0:
        with open("user.json","w",encoding="utf-8") as fp:
            json.dump([],fp)
        id,Password=user_name_password()
        password1,password2=password_hexdigest(Password)#1为未加密的，2为加密后的密码
        save_password(password1)
        user={
            f'{id}':f'{password2}',
        }
        user_list=[user]
        with open("user.json","w",encoding="utf-8") as fp:
            json.dump(user_list,fp)
    with open("user.json","r",encoding="utf-8") as fp:
        list_dictionary=json.loads(fp.read())
        dictionary=list_dictionary[0]
    password1=read_password()
    for i in dictionary.keys():
        User=[i,password1]  
    return User


def simulate(id,Password):#模拟浏览器登录校园网
    #不直接退出浏览器的方法
    # option=webdriver.EdgeOptions()
    # option.add_experimental_option("detach",True)
    # browser=webdriver.Edge(options=option)
    browser=webdriver.Edge()#直接退出浏览器
    browser.get("http://172.30.21.100/tpl/whut/login.html?acip=172.30.1.223&acname=WHUT-Bras-ME60-A&ip=10.84.131.112&nasId=52&userip=10.84.131.112&wlanacname=")

    #根据标签By.ID（找到<input>中去了）去查找ID的值value（即元素)，返回一个WebElement对象，这个对象有一个click（）方法，模拟鼠标在该元素上单击
    #ID具有唯一性
    user_name=browser.find_element(by=By.ID,value="username")
    password=browser.find_element(by=By.ID,value="password")
    btn=browser.find_element(By.ID,"login-account")

    #给Web页面的文本字段发送按键事件信息。找到那个文本字段的<input>元素，send_keys("")方法为输入的按键消息
    user_name.send_keys(id)
    password.send_keys(Password)

    #模拟单击（webelement方法）
    btn.click()

    browser.close()





def main():
    user_massage=user_exist()
    id,Password=user_massage
    simulate(id,Password)
    os.system("cls")
    ansi.text_color(31)
    print("登录成功")
    ansi.text_reset()
    time.sleep(1)
    quit()


if __name__=="__main__":
    main()

















