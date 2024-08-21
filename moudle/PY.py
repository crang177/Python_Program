

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
        