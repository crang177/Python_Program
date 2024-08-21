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
            quit()

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
    user_name=input('用户名：')
    gotoxy(14,11)
    user_password=input('密 码：')
    user={
        'user_name':user_name,
        'user_password':user_password,
    }

    
    gotoxy(18,13)
    print("[1]创建     [2]返回")

    print('                        (   ) ')
    gotoxy(27,14)
    Create_number=eval(input())

    
    if Create_number==1:
        User_Creation(user)

    else:
        os.system('cls')
        Fengmian()





def User_Creation(User):#用户创建函数，文件读写操作
    while True:
        path=Path('D:/GitHub data/py\Python_Program/Json/Users.json')
        with open(path,'r+') as fp1:
            List_json=json.loads(fp1)
            Users_List=List_json.readlines()
            
        if User not in Users_List:
            with open(path,'a') as fp2:
                json.dump(User+'\n',fp2)
            break
                
        else:
            
                gotoxy(15,8)
                print('该用户已存在，请重新输入')
                User_Registrated()
                break



                  




















    