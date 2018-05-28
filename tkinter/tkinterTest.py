import tkinter

win=tkinter.Tk()
win.title("SUCC")

win.geometry("400x400+200+200")

# def updata():
#     message=""
#     if hobby1.get()==True:
#         message+="money\n"
#     if hobby2.get() == True:
#         message += "power\n"
#     if hobby3.get() == True:
#         message += "people\n"
#     text.delete(0.0,tkinter.END)
#     text.insert(tkinter.INSERT, message)
#
#
# hobby1=tkinter.BooleanVar()
# check1=tkinter.Checkbutton(win,text="money",variable=hobby1,command=updata)
# check1.pack()
#
# hobby2=tkinter.BooleanVar()
# check2=tkinter.Checkbutton(win,text="power",variable=hobby2,command=updata)
# check2.pack()
#
# hobby3=tkinter.BooleanVar()
# check3=tkinter.Checkbutton(win,text="people",variable=hobby3,command=updata)
# check3.pack()
#
# # 单选框
# def show():
#     print(r.get())
# text=tkinter.Text(win,width=50,height=5)
# text.pack()
#
# r=tkinter.IntVar()
# radio1=tkinter.Radiobutton(win,text="one",value=1,variable=r,command=show)
# radio1.pack()
#
# radio2=tkinter.Radiobutton(win,text="two",value=2,variable=r,command=show)
# radio2.pack()
#
# # SINGLE='single'
# # BROWSE='browse'
# # MULTIPLE='multiple'
# # EXTENDED='extended'
# lbv=tkinter.StringVar()
# lb=tkinter.Listbox(win,width=100,selectmode=tkinter.MULTIPLE,listvariable=lbv)
#
# for item in["good","good2","good3","good","good2","good3","good","good2","good3","good","good2","good3","good","good2","good3","good","good2","good3","good","good2","good3"]:
#     lb.insert(tkinter.END,item)
# # 滚动条
# sc=tkinter.Scrollbar(win)
# sc.pack(side=tkinter.RIGHT,fill=tkinter.Y)
# sc.pack()
# sc['command']=lb.yview()
#
# lb.insert(tkinter.ACTIVE,"cool")
# lb.configure(yscrollcommand=sc.set)
# lb.pack(side=tkinter.LEFT,fill=tkinter.BOTH)
# # print(lbv.get())
# def myPrint(event):
#     print("+++++++")
#     for item in lb.curselection():
#         print(lb.get(item))
#
# lb.bind("<<ListboxSelect>>",myPrint)
# lbv.set(("23","42","123"))

# lb.delete(0,2)

# lb.select_set(0,2)

# lb.select_clear(1)
# 获取到列表里面的个数
# print(lb.size())
#
# print(lb.get(2))
# print(lb.get(1,2))
# print(lb.curselection())
# print(lb.select_includes(2))


#
# HORIZONTAL
# VERTICAL
scalel=tkinter.Scale(win,from_=0,to=1000,orient=tkinter.HORIZONTAL,tickinterval=500,length=200)
scalel.pack()
win.mainloop()

