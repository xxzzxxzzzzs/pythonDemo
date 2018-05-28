import  tkinter
from  tkinter import  ttk
import  os

class treeWin(tkinter.Frame):
    def __init__(self,master,path):
        frame=tkinter.Frame(master)
        frame.pack()

        self.tree=ttk.Treeview(frame)
        self.tree.pack()
        print(os.path.splitext(path))
        root=self.tree.insert("","end",text=os.path.splitext(path),open=True)



