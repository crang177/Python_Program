import os
import json
from pathlib import Path



def gotoxy(x,y):#光标移动函数，利用了ANSI转义序列（跟操作系统和终端有关）
    print(f'\033[{y};{x}H',end="")






def Jiemian(m,n):#界面函数
    for i in range(m):
        gotoxy(i+1,1)
        print("*",end="")
    for i in range(n):
        gotoxy(1,i+1)
        print("*",end="")
    for i in range(n):
        gotoxy(m,i+1)
        print("*",end="")
    for i in range(m):
        gotoxy(i+1,n)
        print("*",end='')







def Fengmian():#第一个界面函数
    Jiemian(56,20)

    gotoxy(15,4)
    print('学生成绩管理系统（简易版）')

    gotoxy(20,9)
    print("(1)注册")

    gotoxy(20,11)
    print("(2)登录")

    gotoxy(20,13)
    print("(3)退出")

    gotoxy(7,21)
    print('请输入数字1,2或者3: [          ]')

    gotoxy(29,21)
    n=input()  

    return n





def Judgement_First(Select_type):#判断第一个界面函数的输出值，选择进入模式
    while True:
        if Select_type=="1":
            os.system('cls')
            User_Registrated()
            break;

        elif Select_type=="2":
            os.system('cls')
            User_Logined()
            break

        elif Select_type=="3":
            quit()
        else:
            os.system('cls')
            Select_type=Fengmian();







def User_Registrated():#注册用户
    
    Jiemian(56,20)

    gotoxy(15,4)
    print('学生成绩管理系统（简易版）')


    gotoxy(11,7)
    print('-----------------------------------')
    gotoxy(11,16)
    print('-----------------------------------')

    for i in range(8):
        gotoxy(11,i+8)

        print('|',end='')
    for i in range(8):
        gotoxy(46,i+8)
        print('|',end='')

    user={}    
    gotoxy(14,9)
    user_name=input('用户名：')#获得用户名字，将值赋给字典user_new中的键'name'
    gotoxy(14,11)
    user_password=input('密 码：')
    user_new={
        'name':user_name,
        'password':user_password,
    }

    
    gotoxy(18,13)
    print("[1]创建     [2]返回")

    print('                        (   ) ')
    gotoxy(27,14)
    Create_number=input()

    
    if Create_number=='1':
        User_Creation(user_new)

    else:
        os.system('cls')
        Fengmian()
        Select_type=Fengmian()
        Judgement_First(Select_type)





def User_Creation(User_new):#用户注册函数，文件读写操作，参数是一个字典，包含了用户的名字和密码
    while True:
        Q=0#用来判断是否有重复用户名，Q的主要作用是在用重复用户名时不执行将重复的用户名追加到列表末尾Users_List.append(User_new)
        path=Path('D:/GitHub data/py\Python_Program/Json/Users.json')
        with open(path,'r+') as fp1:#访问模式r+表示可以读写，文件指针在文件开头
            Users_List=json.loads(fp1.read())#json.loads返回得到一个列表，目的是获得字典列表，刚开始时要手动输入一个[]
            #使用json.load(文件名)，再利用异常语句try-except：打开成功就获得一个列表，打开文件失败则返回一个空列表
            #Users_List用于接收json.loads(fp1.read())返回的python列表

        for user in Users_List:#遍历列表Users_List，查看注册的用户名是否重复
            if User_new['name']==user['name']:#当输入用户的名字与储存的用户名有重复时
                os.system('cls')#清屏
                gotoxy(15,8)
                print('该用户已存在，请重新输入')
                User_Registrated()#重复注册用户的操作
                Q=1
                break
        if Q==1:
            continue
        
        Users_List.append(User_new)#将输入的用户名追加到列表Users_List中
        break

    with open(path,'w') as fp2:#将追加以后得到的列表Users_List储存到文件中
        json.dump(Users_List,fp2)

    os.system('cls')#注册用户完成以后，清屏并回到第一个界面函数，并输入界面函数对应函数
    Select_type=Fengmian()
    Judgement_First(Select_type)






def User_Logined():#登录用户函数
    Jiemian(56,20)

    gotoxy(15,4)
    print('学生成绩管理系统（简易版）')


    gotoxy(11,7)
    print('-----------------------------------')
    gotoxy(11,16)
    print('-----------------------------------')

    for i in range(8):
        gotoxy(11,i+8)

        print('|',end='')
    for i in range(8):
        gotoxy(46,i+8)
        print('|',end='')

      
    gotoxy(14,9)
    user_name=input('用户名：')#获得用户名字，将值赋给字典user_logined中的键'name'
    gotoxy(14,11)
    user_password=input('密 码：')
    user_login={
        'name':user_name,
        'password':user_password,
    }

    
    gotoxy(18,13)
    print("[1]登录     [2]返回")

    print('                        (   ) ')
    gotoxy(27,14)
    Create_number=input()

    
    if Create_number=='1':
        pass

    else:
        os.system('cls')
        Fengmian()
        Select_type=Fengmian()
        Judgement_First(Select_type)






def User_login_file():#登陆时访问json文件，读取用户信息和密码
    



                  




















    