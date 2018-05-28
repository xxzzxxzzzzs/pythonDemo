
class Preson(object):

    name =""
    age =0
    height =0
    weight =0
    # self类的实例化
    def __init__(self ,name ,age,height,weight):
        self.name =name
        self.age =age
        self.height =height
        self.weight =weight
        pass
    def run(self):
        print("run")
    def eat(self ,food):
        print("eat " +food)
    def __del__(self):
        print("释放")
        pass
    def __repr__(self):
        return "%s %d %d %d"%(self.name,self.age,self.weight,self.height)
    def __str__(self):
        return "%s %d %d %d"%(self.name,self.age,self.weight,self.height)

f=Preson(name="1213",age=12,height=100,weight=100)
print(f)

def func():
    per=Preson(name="1213",age=12,height=100,weight=100)
# func()

