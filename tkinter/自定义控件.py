import  tkinter
from  TreeWin import treeWin
win= tkinter.Tk()
win.title("main")
win.geometry("900x400+200+50")
path="/Users/zzs/Desktop/往期项目/ershou_ios"
treeWin=treeWin(win,path)

win.mainloop()

