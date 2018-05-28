import tkinter

def func(event):
    print("鼠标左键点击")
def func2(event):
    print("点击")
win=tkinter.Tk()
win.title("SUCC")

win.geometry("400x400+200+200")
lable=tkinter.Label(win,text="asdas")
lable.bind("<Double-Button-2>",func2)
lable.pack()
button=tkinter.Button(win,text="鼠标左键点击")
button.bind("<Button-1>",func)
button.pack()
def Move(event):
    print(event.x,event.y)
button2=tkinter.Button(win,text="鼠标左键点击")
button2.bind("<B1-Motion>",Move)
button2.pack()
def func3(event):
    print("组合按键")
# 组合按键事件
win.bind("<Command-o>",fun3)








# Double-Button-2 点击次数 ，左键 右键
win.mainloop()