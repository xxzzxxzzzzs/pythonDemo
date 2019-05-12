import urllib.request
import  re
import os
import time
import  random
import  ssl
#-*- coding:utf-8 -*-
def downImg(url,topath,txtpath,page):
    # header={
    #     "User-Agent": "Mozilla/5.0 (iPad; CPU OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"
    # }
    agentList = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"]
    # headers={
    #     "User-Agent":random.choice(agentList)
    # }
    agent = random.choice(agentList)
    req2 = urllib.request.Request(url)
    req2.add_header("User-Agent", agent)
    # 创建未验证的上下文
    context = ssl._create_unverified_context()
    response2 = urllib.request.urlopen(req2, context=context)
    httpStr = response2.read().decode("utf-8")
    # req=urllib.request.Request(url,headers=header)
    # res=urllib.request.urlopen(req)
    # httpStr=res.read().decode("utf-8")
    # print(httpStr)
    # pat = r'src="//(.*?)"'

    pat = r"data-photo-modal-image-download-link='(.*?)'"
    # pat ='src="(.*?)\.jpg"'
    re_imgs = re.compile(pat,re.S)
    imgs = re_imgs.findall(httpStr)

    print(len(imgs))
    num=1

    for imgurl in imgs:
        with open(txtPath,"a") as f:
            f.write(str(imgurl)+'\r\n')

    for imgurl in  imgs:
        path=os.path.join(topath,str(page)+"_"+str(num)+".jpg")
        num+=1
        # 下载
        if num%4==0:
            time.sleep(3)
        try:
            print(imgurl)
            # urllib.request.urlretrieve(imgurl, filename=path)
            req3 = urllib.request.Request(imgurl)
            req3.add_header("User-Agent", agent)
            # 创建未验证的上下文
            context2 = ssl._create_unverified_context()
            response3 = urllib.request.urlopen(req3, context=context2)
            cat_img = response3.read()
            # imgres = req3.get(imgurl)
            with open(path, 'wb') as f:
                f.write(cat_img)
        except :
              print("12346567")
    # with open(topath,"wb") as  f:
    #     f.write(httpStr)



downPath=r"D:\img\imgs"
txtPath=r"D:\img\imgs.txt"
httpurl="https://www.pexels.com/search/technology/"
page=1
for page in range(1,30):
    httpurlpage=httpurl+"?page="+str(page)
    downImg(httpurlpage,downPath,txtPath,page)



  # < img src = "//img12.360buyimg.com/n7/s230x230_jfs/t20080/13/1109926765/365024/fc511010/5b15481aNe24175e9.jpg!cc_230x230.jpg" >