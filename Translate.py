from translate import Translator
import tkinter as tk

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

    def btn1_language(self):#第一个确认按钮的函数,返回一个translator对象
        from_lang=self.entry1.get().capitalize()#将首字母大写，其余都小写
        to_lang=self.entry2.get().capitalize ()
        translator=Translator(from_lang=from_lang,to_lang=to_lang)
        return translator
        

    def btn2_translate(self):#翻译
        translator=self.btn1_language()
        text=self.text1.get(0.0,"end")
        text_translate=translator.translate(text)

        self.text2.insert(0.0,text_translate)#将文本框的文本翻译好后的文本插入文本框2,第一个参数为插入的位置,第二个为插入的字符串

    def btn3_clear(self):#清空输入翻译和输出翻译的文本框
        self.text1.delete(1.0,"end")
        self.text2.delete(1.0,"end")
                             
                             
                             
                             
                             
                             




if __name__=="__main__":
    a=GUi()
    a.root.mainloop()
