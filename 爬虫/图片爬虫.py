import urllib.request
import  re
import os
import time

#-*- coding:utf-8 -*-
def downImg(url,topath,txtpath):
    header={
        "User-Agent": "Mozilla/5.0 (iPad; CPU OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"
    }

    req=urllib.request.Request(url,headers=header)
    res=urllib.request.urlopen(req)
    httpStr=res.read().decode("utf-8")
    # print(httpStr)
    pat = r'src="//(.*?)"'
    # pat ='src="(.*?)\.jpg"'
    re_imgs = re.compile(pat,re.S)
    imgs = re_imgs.findall(httpStr)

    print(len(imgs))
    num=1
    for imgurl in imgs:
        with open(txtPath,"a") as f:
            f.write(str(imgurl)+'\r\n')

    for imgurl in  imgs:
        path=os.path.join(topath,str(num)+".jpg")
        num+=1
        # 下载
        if num%20==0:
            time.sleep(3)
        try:
            urllib.request.urlretrieve("http://" + imgurl, filename=path)
        except :
              print("12346567")


    with open(topath,"wb") as  f:
        f.write(httpStr)



downPath=r"C:\Users\Administrator\Desktop\img\img3"
txtPath=r"C:\Users\Administrator\Desktop\img\imgs.txt"
httpurl="http://search.yhd.com/c0-0/k%25E5%2586%2585%25E8%25A1%25A3"
downImg(httpurl,downPath,txtPath)



  # < img src = "//img12.360buyimg.com/n7/s230x230_jfs/t20080/13/1109926765/365024/fc511010/5b15481aNe24175e9.jpg!cc_230x230.jpg" >