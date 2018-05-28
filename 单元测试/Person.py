class Person(object):
    def __init__(self,name,age,):
        self.name=name
        self.age=age

    def getVar(self,v):
        print(self(v))

        return self(v)

    def getName(self):
        return self.name