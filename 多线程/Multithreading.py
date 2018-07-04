# 1 多线程
# 2 多进程
# 3 协程模式
# 4 多进程+  多线程

# 进程 都有自己的数据段 代码段 堆栈段
from time import sleep
from  multiprocessing import  Process
import  os

def fun(str):
    while True:
        print("good"+str+"=====%s"%os.getpid())
        print(os.getppid())
        sleep(1.2)

# 单任务现象
# if __name__ == "__main__":
#     while True:
#         print("suck")
#         sleep(1)
#     # 只有上面执行完毕才执行
#     fun()


if __name__ == "__main__":

    print("主进程")
    # 创建子进程
    p=Process(target=fun,args=("nice",))
    p.start()
    while True:
        print("suck"+"=====%s"%os.getpid())
        sleep(1)
