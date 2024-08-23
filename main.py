from moudle import PY
import os  #引入os模块
import json
from pathlib import Path




os.system('cls')#清屏操作
 

Select_type_1=PY.Fengmian()#登录和注册
PY.Judgement_First(Select_type_1);
Select_type_2=PY.Fengmian_2()#查看和编辑学生成绩
PY.Judgement_Second(Select_type_2)



# path=Path('D:/GitHub data/py/Python_Program/txt/Students_Achievemrn.txt')
# ren={
#     'name':'ghgasd',
#     'ch':21,
#     'math':54,
#     'english':46,
#     'Grade_point_average':55

# }
# with open(path,'a') as fp:
#     c=0
#     for i in ren.values():
#             c+=1
#             if c!=5:
#                   fp.write(f'{i}    ')
#             else:
#                   fp.write(f'{i}\n')
    





# path=Path('D:/GitHub data/py/Python_Program/txt/Students_Achievemrn.txt')
# Row=2#行数
# with open(path,'r') as fp3:
#     Student_grades_List=fp3.read().splitlines()

# print(Student_grades_List)


# if Student_grades_List :
#     #os.system('cls')
#     #print('          语文    数学    英语    平均成绩')
#     for Student_grades in Student_grades_List:
#         PY.gotoxy(4,Row)
#         print(f'{Student_grades}')
#         Row+=1




    



        
    
        
        





















        
    


    
# if User not in Users_List:
#     with open(path,'a') as fp2:
#         json.dump(User,fp2)
    
        
# else:
    
#         gotoxy(15,8)
#         print('该用户已存在，请重新输入')
#         User_Registrated()
        
