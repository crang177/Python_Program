from moudle import PY
import os  #引入os模块
import json
from pathlib import Path




os.system('cls')#清屏操作
 

Select_type_1=PY.Fengmian()#登录和注册
PY.Judgement_First(Select_type_1);
Select_type_2=PY.Fengmian_2()#查看和编辑学生成绩
PY.Judgement_Second(Select_type_2)



















       
    


















    



        
    
        
        





















        
    


    
# if User not in Users_List:
#     with open(path,'a') as fp2:
#         json.dump(User,fp2)
    
        
# else:
    
#         gotoxy(15,8)
#         print('该用户已存在，请重新输入')
#         User_Registrated()
        
