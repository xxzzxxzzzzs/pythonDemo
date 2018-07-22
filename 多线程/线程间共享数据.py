# 多线程和多进程最大的不同，多进程中，同一个变量，各自存在一个拷贝在每个进程中，互不影响
# 多线程中所有变量都由 线程共享，所以任何一个变量都可以被人以一个线程修改
# 线程间共享数据 最大的危险危险在于线程同时更改一个变量 ，容易吧内容该乱了
import threading
import time
num=0

# 线程锁  加锁 必须释放锁
# 阻止了线程的并发执行 包含锁的代码实际上只能以单进程的模式执行，所以效率大大的降低的
# 由于可以存在多个锁 不同线程持有不同的锁，并试图获取其他锁，可以造成死锁 导致多个线程挂起
lock=threading.Lock()
def run(other):
    global num;
    for i in range(10000000):
        # # 加锁
        # lock.acquire();
        # try:
        #     num = num + other
        #     # time.sleep(0.5)
        #     num = num - other
        # finally:
        #     # 释放锁
        #     lock.release();
        with lock:
             num = num + other
             num = num - other
        # 会自动上锁并且解锁
            


def run2(other):
    global num;
    for i in range(10000000):
        lock.acquire();
        try:
            num = num - other
            # time.sleep(0.6)
            num = num+other
        finally:
            lock.release();
        # time.sleep(1)

        # print(other)

if __name__=="__main__":

    t=threading.Thread(target=run,args=(24,))
    t2 = threading.Thread(target=run2,args=(333,))
    t2.start()
    t.start()
    t.join()
    t2.join()

    print("num="+ str(num) )