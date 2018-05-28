import os
import  collections
# -*- coding: UTF-8 -*-

path="/Users/zzs/Desktop/python"
#
def getRecursionAllDir(path,sp=""):
    filesList= os.listdir(path)
    sp+="   "
    for filemane in  filesList:
        if os.path.isdir(os.path.join(path,filemane)):
            print(sp,"目录 :", filemane)
            getRecursionAllDir(os.path.join(path,filemane),sp)

        else:
            print(sp,"文件",filemane)

    pass

# getRecursionAllDir(path)

def getAllDirDE(path):
    stack=[]
    stack.append(path)

    while len(stack)!=0:
        # 出栈
        dirPath=stack.pop()
        dirList=os.listdir(dirPath)
        for filemane in dirList:
            if os.path.isdir(os.path.join(dirPath, filemane)):
                print("目录 :", filemane)
                stack.append(os.path.join(dirPath, filemane))
            else:
                print("文件", filemane)
        pass

    pass

# getAllDirDE(path)
# 队列、
def getAllDirQU(path):
    queue=collections.deque()
    queue.append(path)
    while len(queue)!=0:
        dirPath=queue.pop()
        dirLists=os.listdir(dirPath)
        for filemane in dirLists:
            if os.path.isdir(os.path.join(dirPath, filemane)):
                print("目录 :", filemane)
                queue.append(os.path.join(dirPath, filemane))
            else:
                print("文件", filemane)
        pass
    pass

getAllDirQU(path)