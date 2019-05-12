for multiprocessing import Process

class zzsProcess(Process):
    def __init__(self,name):
        Process.__init__(self)
        self.name=name

    def run(self):
        print("启动%s"%(self.name))
        print(self.name)
        print("结束%s" % (self.name))
