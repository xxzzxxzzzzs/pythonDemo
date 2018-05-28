# -*- coding: UTF-8 -*-
import  os
path="/Users/zzs/Desktop/python/基础/163/filetes3"


def work(path):
    resPath="/Users/zzs/Desktop/python/基础/163/"
    with open(path,"r") as f:
        while True:
            lineInfo=f.readline()
            if len(lineInfo)<5:
              break
            mailStr=lineInfo.split("----")[0]
            password=lineInfo.split("----")[1]
            print(mailStr)
            dirStr=os.path.join(resPath,mailStr.split("@")[1].split(".")[0])
            print(dirStr)
            if not os.path.exists(dirStr):
                os.mkdir(dirStr)
            w = open(os.path.join(dirStr,mailStr.split("@")[1].split(".")[0]+ ".txt"), "a", encoding="utf-8", errors="ignore")
            w.write("账户: "+mailStr+"密码"+password+"\n")
            # w.write("")


work(path)