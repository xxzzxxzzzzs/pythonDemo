from multiprocessing import  Process ,Queue ,Pool
import os,time
import  random
def write(q):
    print("启动写子进程--%s"%os.getpid())
    for chr in ["A","B","C","D"]:
        q.put(chr)
        print("写入"+chr)
        # time.sleep(1)
    print("结束子进程--%s"%os.getpid())


def read(q):
    print("启动读子进程--%s"%os.getpid())
    while True:
        v=q.get(True)
        print("读出v=%s"%v)
def run(i):
    start=time.time()
    end=time.time()
    print("%d子进程%s耗时%f"%(i,os.getpid(),(end-start)))





if __name__ == "__main__":
    # 父进程 创建队列 并传递个子进程
    # q=Queue()
    # pw=Process(target=write,args=(q,))
    # pr = Process(target=read, args=(q,))
    # pr.start()
    # pw.start()
    #
    # # 父进程的结束不能影响子进程 让父进程等待子进程结束后在执行
    # pw.join()
    #
    # pr.terminate()
    #
    # print("父进程结束")



    pp=Pool(2)
    for i in range(10):
        pp.apply_async(run,args=(i,))
    # close 后不能加新进程
    pp.close()
    # 进程池里面的进程全部结束结束进程
    pp.join()

    print("父进程结束")
