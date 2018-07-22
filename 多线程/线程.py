# 一个进程内部 同事干多件事情 子任务为线程
# 线程通常叫做轻型进程 线程共享内存空间并发执行任务 ，每个线程共享一个进程的资源
# 线程是最小的执行单元，而进程由至少一个线程组成，如何电镀进程和线程，完全由操作系统决定，程序不能决定什么时候执行


# 模块 _thread  底层模块
# threading模块  封装模块
import  threading
import  time
def run(name):
    print("线程启动 %s" % (threading.current_thread().name))
    time.sleep(2)
    print("name=%s"%name)
    print("线程结束 %s" % (threading.current_thread().name))

if __name__=="__main__":
    # 任何进程默认都会启动一个线程，成为主线程，主线程可以启动子线程
    print("主线程启动 %s"%(threading.current_thread().name))

    t=threading.Thread(target=run,name="线程名称007",args=("lalala",));
    t.start()
    # 确保在主线程结束执行
    t.join()

    print("主线程结束 %s" % (threading.current_thread().name))