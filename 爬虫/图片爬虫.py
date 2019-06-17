import urllib.request
import  re
import os
import time
import  random
import  ssl
#-*- coding:utf-8 -*-
def downImg(url,topath,txtpath,page,searchPath):
    # header={
    #     "User-Agent": "Mozilla/5.0 (iPad; CPU OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"
    # }
    agentList = [
        # IPhone
        "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
        # IPod
        "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
        # IPAD
        "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
        "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
        # Android
        "Mozilla/5.0 (Linux; U; Android 2.2.1; zh-cn; HTC_Wildfire_A3333 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        # QQ浏览器 Android版本
        "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        # Android Opera Mobile
        "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
        # Android Pad Moto Xoom
        "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
        # BlackBerry
        "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
        # WebOS HP Touchpad
        "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
        # Nokia N97
        "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
        # Windows Phone Mango
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
        # UC浏览器
        "UCWEB7.0.2.37/28/999",
        "NOKIA5700/ UCWEB7.0.2.37/28/999",
        # UCOpenwave
        "Openwave/ UCWEB7.0.2.37/28/999",
        # UC Opera
        "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999"
        ]
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
    isExists = os.path.exists(topath+searchPath)
    if not isExists:
        os.mkdir(topath+searchPath)

    for imgurl in  imgs:
        path=os.path.join(topath+searchPath,str(page)+"_"+str(num)+".jpg")
        num+=1
        # 下载
        if num%6==0:
            time.sleep(2)
        try:
            print(imgurl)
            # urllib.request.urlretrieve(imgurl, filename=path)
            req3 = urllib.request.Request(imgurl)
            req3.add_header("User-Agent", agent)
            # 创建未验证的上下文
            context2 = ssl._create_unverified_context()
            response3 = urllib.request.urlopen(req3, context=context2,timeout=1)
            cat_img = response3.read()
            # imgres = req3.get(imgurl)
            with open(path, 'wb') as f:
                f.write(cat_img)
        except :
              print("12346567")
    # with open(topath,"wb") as  f:
    #     f.write(httpStr)



downPath=r"D:\img\imgs"
searchPath=r"Sculpture"
txtPath=r"D:\img\imgs.txt"
httpurl="https://www.pexels.com/search/"
page=1
for page in range(1,30):
    httpurlpage=httpurl+searchPath+"?page="+str(page)
    downImg(httpurlpage,downPath,txtPath,page,searchPath)



  # < img src = "//img12.360buyimg.com/n7/s230x230_jfs/t20080/13/1109926765/365024/fc511010/5b15481aNe24175e9.jpg!cc_230x230.jpg" >