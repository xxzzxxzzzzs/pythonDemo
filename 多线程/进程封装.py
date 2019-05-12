from zzsProcess import zzsProcess

if __name__ =="__main__":

    print("父进程")

    p=zzsProcess("test")

    p.start()