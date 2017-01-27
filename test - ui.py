from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog
import os

def ui_process():
    root =Tk()
    root.geometry("300x400+500+500")

    L_titile = Label(root,text='沈力风机股份有限公司',)
    L_titile.config(font='Helvetica -15 bold',fg='blue')
    L_titile.place(x=150,y=20,anchor="center")
    L_author = Label(root, text='作者:LCC')
    L_author.config(font='Helvetica -10 bold')
    L_author.place(x=250,y=380)

    B_0 = Button(root, text="对话框", command=CreatDialog)
    B_0.place(x=90,y=200)
    B_1 = Button(root, text="确定", command=print)
    B_1.place(x=150, y=200)
    B_OK = Button(root,text="创建",command=lambda:button_process(root))
    B_OK.place(x=200,y=200)
    B_NO = Button(root, text="取消")
    B_NO.place(x=250,y=200)

    v = IntVar()
    R_ONE=Radiobutton(root, text="One", variable=v, value=1,command=lambda:Print_b(1)).place(x=60,y=150)
    R_TWO=Radiobutton(root, text="Two", variable=v, value=2,command=lambda:Print_b(2)).place(x=10,y=150)

    W = Scale(root, from_=0, to=100,orient=HORIZONTAL)#orient=HORIZONTAL 横向，默认纵向
    W.place(x=50,y=300)
    # print(W.get())  #获取滑块值

    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Open", command=OpenFile)
    filemenu.add_command(label="Save", command=SaveFile)
    # filemenu.add_separator()#分割线
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    root.config(menu=menubar)

    mainloop()

def button_process(root):
    messagebox.askokcancel('Python Tkinter', '确认创建窗口？')
    messagebox.askquestion('Python Tkinter', "确认创建窗口?")
    messagebox.askyesno('Python Tkinter', '是否创建窗口？')
    messagebox.showerror('Python Tkinter', '未知错误')
    messagebox.showinfo('Python Tkinter', 'hello world')
    messagebox.showwarning('Python Tkinter', '电脑即将爆炸，请迅速离开')
    root1 = Toplevel(root)

def PrintHello():
    print("hello")

def Print_b(a):
    print(a)

def CreatDialog():
    world = simpledialog.askstring('Python Tkinter', 'Input String', initialvalue = 'Python Tkinter')
    print(world)
    # simpledialog.askinteger()
    # simpledialog.askfloat()

def OpenFile():
    f = filedialog.askopenfilename(title='打开文件', filetypes=[('Python', '*.py *.pyw'), ('All Files', '*')])
    print(f)
    #使用os 模块运行
def SaveFile():
    f = filedialog.asksaveasfilename(title='保存文件', initialdir='d:\mywork', initialfile='hello.py')
    print(f)
    #调用OS模块
if __name__ == "__main__":
    print("开始")
    ui_process()