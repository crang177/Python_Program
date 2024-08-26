import os
import json
from pathlib import Path





if os.name=='nt' :
    os.system('')#启用ANSI转义序列




# def cursor_fixed(max_char):#光标固定函数
#     import sys

# if os.name == 'nt':
#     os.system('')

# max_char=3
# input_char=''

# while len(input_char)<max_char:
#     char=input()
#     if len(input_char) < max_char:
#         if char:
#             input_char=char[0]
#             print(char[0], end='', flush=True)

#         else:
#             print('\033[D', end='', flush=True)
# print()
# print(input_char)




    
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
            os.system('cls')
            print("学生成绩管理系统（简易版）已关闭")
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

    elif Create_number=='2':
        os.system('cls')
        Fengmian()
        Select_type=Fengmian()
        Judgement_First(Select_type)
    else :
        os.system('cls')
        User_Registrated()






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
        json.dump(Users_List,fp2,indent=2)#indent=4表示缩进

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
        User_login_file(user_login)

    elif Create_number=='2':
        os.system('cls')
        Fengmian()
        Select_type=Fengmian()
        Judgement_First(Select_type)
    else:
        os.system('cls')
        User_Logined()







def User_login_file(user_login):#登陆时访问json文件，读取用户信息和密码
    path=Path('D:/GitHub data/py/Python_Program/Json/Users.json')
    with open(path,'r') as fp2:
        User_List=json.loads(fp2.read())

    while True :
        count_name=0

        for user in User_List :
            if (user['name'])==user_login['name']:
                User_name_Exist=1#用户名存在于文件时赋值为1
                
            else :
                count_name+=1
            if count_name==len(User_List) :#当未查找的次数为列表的元素数量时
                User_name_Exist=2#当用户名不存在时赋值为2


            if user['password']==user_login['password']:#判断密码
                User_password_right=1#正确赋值为1
                break
                
            else :
                User_password_right=2#错误赋值为2
                
        if User_name_Exist==1 and User_password_right==1:#登录成功
            os.system('cls')
            break
        else :#登录失败
            os.system('cls')
            gotoxy(15,8)
            print('用户名或密码错误，请重输')
            User_Logined()
            break







def Fengmian_2():#登录完成后的界面函数
    Jiemian(56,20)

    gotoxy(15,4)
    print('学生成绩管理系统（简易版）')

    gotoxy(20,9)
    print("(1)查看学生成绩")

    gotoxy(20,11)
    print("(2)编辑学生成绩")

    gotoxy(20,13)
    print("(3)退出")

    gotoxy(7,21)
    print('请输入数字1,2或者3: [          ]')

    gotoxy(29,21)
    n=input()  

    return n







def Judgement_Second(Select_type_2):#判断选择是查看，还是编辑学生成绩
    while True:
        if Select_type_2=="1":
            os.system('cls')
            View_student_grades()#查看学生成绩
            break

        elif Select_type_2=="2":
            os.system('cls')
            Edit_student_grades()#编辑学生成绩
            break

        elif Select_type_2=="3":
            os.system('cls')
            print("学生成绩管理系统（简易版）已关闭")
            quit()
        else:
            os.system('cls')
            Select_type_2=Fengmian_2();







def Fengmian_3():#查看学生成绩的界面函数
    Jiemian(56,20)

    gotoxy(15,4)
    print('学生成绩管理系统（简易版）')

    gotoxy(15,9)
    print("请输入要查看学生成绩的班级：")

    gotoxy(15,10)
    print("(              )")

    gotoxy(15,11)
    print("( 例如: Class_1 )")

    gotoxy(17,10)
    class_which=input()  

    return class_which








class Student_grades:
    def __init__(self,id,name,chinese,math,english):
        self.id=id
        self.name=name
        self.chinese=chinese
        self.math=math
        self.english=english


def View_student_grades():#按班级查看学生成绩
    class_name=Fengmian_3()
    with open(f'D:/GitHub data/py/Python_Program/Sudent_grades_Class/{class_name}.json','a') as fp:
              pass
    path=Path(f'D:/GitHub data/py/Python_Program/Sudent_grades_Class/{class_name}.json')
    if os.path.getsize(path)==0:
        with open(path,'w') as fp:
            json.dump([],fp)

    with  open(path,'r') as fp:
        Student_grades_List=json.loads(fp.read())
    if Student_grades_List==[]:
        os.system('cls')
        print("无学生成绩在系统中")
        fanhui=input('输入1返回：')
        if fanhui=='1':
            os.system('cls')
            Select_type_2=Fengmian_2()
            Judgement_Second(Select_type_2)
    else:
        Row=2#行数
        location=0
        os.system('cls')
        print('  id      姓名          语文    数学    英语    平均成绩')
        print()
        for i in Student_grades_List:
            for j in  i.values():
                location+=1
                if location==1:
                    gotoxy(1,Row)
                    print(f'{j}',end='')
                elif location==2:
                    gotoxy(11,Row)
                    print(f'{j}',end='')
                elif location==3:
                    gotoxy(25,Row)
                    print(f'{j}',end='')
                elif location==4:
                    gotoxy(33,Row)
                    print(f'{j}',end='')
                elif location==5:
                    gotoxy(41,Row)
                    print(f'{j}',end='')
                elif location==6:
                    gotoxy(49,Row)
                    print(f'{j}')
            location=0
            Row+=1

        print()
        while True:
            fanhui=input('输入1返回: ')
            if fanhui=='1':
                os.system('cls')
                Select_type_2=Fengmian_2()
                Judgement_Second(Select_type_2)
                break
            else:
                print('\033[k')#清除当前行
                

        
        


                








def Class_max_score(Student_grades_List):#班级最高分数
    pass

def Class_min_score(Student_grades_List):#班级最低分数
    pass
def Class_average_score(Student_grades_List):#班级平均分数
    pass






































































def Fengmian_4():#编辑学生成绩的封面函数
    Jiemian(56,20)

    gotoxy(15,4)
    print('学生成绩管理系统（简易版）')

    gotoxy(20,9)
    print("(1)修改学生成绩")

    gotoxy(20,11)
    print("(2)添加学生成绩")

    gotoxy(20,13)
    print("(3)删除学生成绩")

    gotoxy(20,15)
    print("(4)返回")

    gotoxy(7,21)
    print('请输入数字1,2,3或者4: [          ]')

    gotoxy(31,21)
    n=input()  

    return n








def Edit_student_grades():#编辑学生成绩
    Select_type_3=Fengmian_4()
    Judgement_Third(Select_type_3)

            
        
        
    


def Judgement_Third(Select_type_3):#判断选择是修改，还是添加学生成绩
    while True:
        if Select_type_3=="1":#修改学生成绩
            Revise_student_grades()
            break
        elif Select_type_3=="2":#添加学生成绩
            class_name=Fengmian_6()
            Add_student_grades(class_name)
            break
        elif Select_type_3=="3":#删除学生成绩
            delete_student_grades()
        elif Select_type_3=="4":#返回
            os.system('cls')
            Select_type_2=Fengmian_2()
            Judgement_Second(Select_type_2)
            break
        else:
            os.system('cls')
            Select_type_3=Fengmian_4()







def Fengmian_5():#修改学生成绩的界面函数
    os.system('cls')
    Jiemian(56,20)

    gotoxy(15,4)
    print('学生成绩管理系统（简易版）')

    gotoxy(15,9)
    print("请输入要修改学生成绩的班级：")

    gotoxy(15,10)
    print("(              )")

    gotoxy(15,11)
    print("( 例如:Class_1 )")

    gotoxy(17,10)
    class_which=input()  

    return class_which










def Revise_student_grades():#修改学生成绩
    class_name=Fengmian_5()
    with open(f'Sudent_grades_Class/{class_name}.json','a'):
        pass
    path=Path(f'Sudent_grades_Class/{class_name}.json')

    if os.path.getsize(path)==0:
        with open(path,'w') as fp:
            json.dump([],fp)
    with open(path,'r') as fp:
        student_grades_list=json.loads(fp.read())

    os.system('cls')
    print("输入要修改成绩的学生的信息:")
    Id_revise=eval(input('  Id:'))
    print('  要修改的科目成绩:')
    print('    (1)语文')
    print('    (2)数学')
    print('    (3)英语')
    gotoxy(3,8)
    print('(输入1,2或者3)')
    gotoxy(1,7)
    subject_revise=input('  输入要修改的科目：')


    list_length=len(student_grades_list)
    number_class_student=0
    if list_length==0:
        os.system('cls')
        print(f'学号为{Id_revise}的学生不存在')
        fanhui=input('输入1返回继续修改,输入2返回至编辑学生成绩界面: ')
        if fanhui=='1':
            os.system('cls')
            Revise_student_grades()
        elif fanhui=='2':
            os.system('cls')
            Select_type_3=Fengmian_4()
            Judgement_Third(Select_type_3)
    else:
        for i in student_grades_list:    
            number_class_student+=1
            if i['Id']==Id_revise:
                os.system('cls')
                if subject_revise=='1':
                    i['Chinese']=eval(input('要修改语文成绩为: '))
                elif subject_revise=='2':
                    i['math']=eval(input('要修改数学成绩为: '))
                elif subject_revise=='3':
                    i['English']=eval(input('要修改英语成绩为: '))
                else:
                    Revise_student_grades()
                i['average']=round((i['Chinese']+i['math']+i['English'])/3,2)

                with open(path,'w') as fp:
                    json.dump(student_grades_list,fp,indent=4)

                print('成绩修改成功！！')
                print()
                fanhui=input('输入1返回继续修改,输入2返回至编辑学生成绩界面: ')
                if fanhui=='1':
                    os.system('cls')
                    Revise_student_grades()
                elif fanhui=='2':
                    os.system('cls')
                    Select_type_3=Fengmian_4()
                    Judgement_Third(Select_type_3) 
                break
            
            if list_length==number_class_student:
                print(f'学号为{Id_revise}的学生不存在')
                fanhui=input('输入1返回继续修改,输入2返回至编辑学生成绩界面: ')
                if fanhui=='1':
                    os.system('cls')
                    Revise_student_grades()
                elif fanhui=='2':
                    os.system('cls')
                    Select_type_3=Fengmian_4()
                    Judgement_Third(Select_type_3) 

                


    















def Fengmian_6():#添加学生成绩的界面函数
    os.system('cls')
    Jiemian(56,20)

    gotoxy(15,4)
    print('学生成绩管理系统（简易版）')

    gotoxy(15,9)
    print("请输入要添加学生成绩的班级：")

    gotoxy(15,10)
    print("(              )")

    gotoxy(15,11)
    print("( 例如:Class_1 )")

    gotoxy(17,10)
    class_which=input()  

    return class_which







def Add_student_grades(class_name):#添加学生成绩
    with open(f'D:/GitHub data/py/Python_Program/Sudent_grades_Class/{class_name}.json','a') as fp:
       pass
    path=Path(f'D:/GitHub data/py/Python_Program/Sudent_grades_Class/{class_name}.json')

    if os.path.getsize(path)==0:#如果path文件为空，则写入一个空列表
        with open(path, 'w') as file:
                json.dump([], file)

    with open(path,'r',encoding='utf-8') as fp:
        student_grades_list=json.loads(fp.read())

    Id_used=0
    while True:
        os.system('cls')
        print("任何时候输入0将退出添加学生成绩,返回编辑学生成绩界面")
        if Id_used==1:
            print('学号已存在，请重新输入！！！')
        Id_used=0
        student={'Id':'','name':'','Chinese':'','math':'','English':'','average':''}

        id=eval(input("学生的ID: "))
        if id==0:
            os.system('cls')
            Select_type_3=Fengmian_4()
            Judgement_Third(Select_type_3)           
        name=input("学生的名字：")
        if name=='0':
            os.system('cls')
            Select_type_3=Fengmian_4()
            Judgement_Third(Select_type_3)
        Chinese=eval(input("学生的语文成绩："))
        if Chinese==0:
            os.system('cls')
            Select_type_3=Fengmian_4()
            Judgement_Third(Select_type_3)
        math=eval(input("学生的数学成绩："))
        if math==0:
            os.system('cls')
            Select_type_3=Fengmian_4()
            Judgement_Third(Select_type_3)
        English=eval(input("学生的英语成绩："))
        if English==0:
            os.system('cls')
            Select_type_3=Fengmian_4()
            Judgement_Third(Select_type_3)
        print()

        student['Id']=id
        for i in student_grades_list:
            if i['Id']==student['Id']:
                Id_used=1
                break
        if Id_used==1:
            continue

        student['name']=name
        student['Chinese']=Chinese
        student['math']=math
        student['English']=English
        student['average']=round((Chinese+math+English)/3,2)

        student_grades_list.append(student)

        with open(path,'w') as fp :
            json.dump(student_grades_list,fp,indent=4)







def Fengmian_7():#删除学生成绩的界面函数
    os.system('cls')
    student_delete=[]
    Jiemian(56,20)

    gotoxy(15,4)
    print('学生成绩管理系统（简易版）')

    gotoxy(15,9)
    print("请输入要删除学生成绩的班级：")

    gotoxy(15,10)
    print("(              )")

    gotoxy(15,11)
    print("( 例如: Class_1 )")
    gotoxy(17,10)
    class_name=input()

    gotoxy(15,13)
    print('请输入要删除学生的id: ')

    gotoxy(15,14)
    print("(                  )")

    gotoxy(17,14)
    Id_delete=eval(input())
    student_delete.append(class_name)
    student_delete.append(Id_delete)
    return student_delete
    

      

def delete_student_grades():
    student_delete=Fengmian_7()
    class_name=student_delete[0]
    Id_delete=student_delete[1]
    
    with open (f'Sudent_grades_Class/{class_name}.json','a') as fp:
        pass
    path=Path(f'Sudent_grades_Class/{class_name}.json')

    if os.path.getsize(path)==0:
        with open(path,'w') as fp:
            json.dump([],fp)

    with open(path,'r') as fp:
        student_grades_list=json.loads(fp.read())
    list_length=len(student_grades_list)
    number_class_student=0

    if list_length==0 :
        os.system('cls')
        print(f'未查找到学号为{Id_delete}的学生成绩')
        fanhui=input('输入1返回继续删除,输入2返回至编辑学生成绩界面: ')
        if fanhui=='1':
            os.system('cls')
            delete_student_grades()
        elif fanhui=='2':
            os.system('cls')
            Select_type_3=Fengmian_4()
            Judgement_Third(Select_type_3)
    
    else:
        for i in student_grades_list:
            number_class_student+=1

            if i['Id']==Id_delete:
                del student_grades_list[number_class_student-1]
                with open(path,'w') as fp:
                    json.dump(student_grades_list,fp,indent=4)
                
                os.system('cls')
                location=0
                print('被删除学生的信息：')
                print('  id      姓名          语文    数学    英语    平均成绩')
                for j in i.values():
                    location+=1
                    if location==1:
                        gotoxy(1,3)
                        print(f'{j}',end='')
                    elif location==2:
                        gotoxy(11,3)
                        print(f'{j}',end='')
                    elif location==3:
                        gotoxy(25,3)
                        print(f'{j}',end='')
                    elif location==4:
                        gotoxy(33,3)
                        print(f'{j}',end='')
                    elif location==5:
                        gotoxy(41,3)
                        print(f'{j}',end='')
                    elif location==6:
                        gotoxy(49,3)
                        print(f'{j}')
                location=0
                print("删除成功！")

                fanhui=input('输入1返回继续删除,输入2返回至编辑学生成绩界面: ')
                if fanhui=='1':
                    os.system('cls')
                    delete_student_grades()
                elif fanhui=='2':
                    os.system('cls')
                    Select_type_3=Fengmian_4()
                    Judgement_Third(Select_type_3) 
                break
            elif list_length==number_class_student :
                os.system('cls')
                print(f'未查找到学号为{Id_delete}的学生成绩')
                fanhui=input('输入1返回继续删除,输入2返回至编辑学生成绩界面: ')
                if fanhui=='1':
                    os.system('cls')
                    delete_student_grades()
                elif fanhui=='2':
                    os.system('cls')
                    Select_type_3=Fengmian_4()
                    Judgement_Third(Select_type_3) 






            










                    
                  













    















    