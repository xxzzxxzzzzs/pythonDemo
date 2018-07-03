import urllib.request
import  ssl
import  os
import  re
from collections import deque
def writeFileBytes(htmlBytes,toPath):
    with open(toPath,"wb") as  f:
        f.write(htmlBytes)

def writeFileStr(htmlBytes,toPath):
    with open(toPath,"wb") as  f:
        f.write(str(htmlBytes))
def getResponse(url):
    header={
        "User-Agent": "Mozilla/5.0 (iPad; CPU OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"
    }

    req=urllib.request.Request(url,headers=header)
    context=ssl._create_unverified_context()
    res=urllib.request.urlopen(req,context=context)
    # print(res.read())
    return res.read()
def qqCrawler(url,toPath):
    htmlBytes=getResponse(url)
    # print(htmlBytes)
    pat="[1-9][0-9]{4,14}"
    re_qq=re.compile(pat)
    qqlist=re_qq.findall(str(htmlBytes))
    # print(len(set(qqlist)))
    for qqstr in set(qqlist):
        print(qqstr)
        with open(toPath, "a") as f:
             f.write(str(qqstr) + '\r\n')
    # print(qqlist)
    # writeFileBytes(htmlBytes,r"C:\Users\Administrator\Desktop\img\qq.html")
    # writeFileStr(htmlBytes,r"C:\Users\Administrator\Desktop\img\qq.txt")

    pass
def runQQlist(baseUrl):
    for i in  range(1,20):
        NewUrl=baseUrl+str(i*100)
        print(NewUrl)
        center(NewUrl,downPath3)
def center(url,topath):
    queue=deque()
    queue.append(url)
    while len(queue)!=0:
        tagUrl=queue.popleft()
        try:
             urlList=qqCrawler(tagUrl,topath)
             if urlList.len >0:
                for item in  urlList:
                  tempUrl=item[0]
                  print(tempUrl)
                  queue.append(str(tempUrl))
        except:
            pass

downPath=r"C:\Users\Administrator\Desktop\img\qq.txt"
url="https://tieba.baidu.com/p/5249938894?pn="
downPath2=r"C:\Users\Administrator\Desktop\img\qq2.txt"
downPath3=r"C:\Users\Administrator\Desktop\img\newQQ.txt"
url2="https://www.douban.com/group/topic/41011762/?start="
# runQQlist(url)

runQQlist(url2)