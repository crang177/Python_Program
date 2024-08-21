from moudle import PY
import os  #引入os模块
import json
from pathlib import Path




os.system('cls')#清屏操作
 

# Select_type=PY.Fengmian()
# PY.Judgement_First(Select_type);




User={
     'name':'bhj',
     'password':'jhbjsf'

}
path=Path('D:/GitHub data/py\Python_Program/Json/Users.json')
with open(path,'r+') as fp1:
    Users_List=json.loads(fp1.read_text())
    print(Users_List)
    #Users_List=Users_List.readlines()
    
# if User not in Users_List:
#     with open(path,'a') as fp2:
#         json.dump(User,fp2)
    
        
# else:
    
#         gotoxy(15,8)
#         print('该用户已存在，请重新输入')
#         User_Registrated()
        
