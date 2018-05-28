# -*- coding: UTF-8 -*-
import  tkinter


win=tkinter.Tk()



win.title("啦啦啦")
win.geometry("400x400+200+20")



# lable
#justify 对其方式
#anchor 位置 center居中 n北
lable=tkinter.Label(win,text="lalafghjhgjjjjjjjjjjjlala"
                    ,bg="pink",
                     fg="blue",
                     font=("黑体",23),
                     width=10,
                    height=10,
                    wraplength=100,
                    justify="left",
                    anchor="w")
lable.pack()
def func():
    lable.config(text='HELLO, WORLD!', font=("", 20))

#button 创建按钮
button=tkinter.Button(win,text="button",command=func)
button.pack()

button2=tkinter.Button(win,text="button",command=lambda  :lable.config(text='3456789'))
button2.pack()



# 输入控件
entry=tkinter.Entry(win)
entry.pack()
button2=tkinter.Button(win,text="button",command=lambda  :lable.config(text=entry.get()))
button2.pack()


















win.mainloop()