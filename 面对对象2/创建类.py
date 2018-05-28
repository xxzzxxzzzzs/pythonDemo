# class 类名（父类列表）:
#     属性
#     行为

# object基类
import json
def convert_to_dict(obj):
    '''把Object对象转换成Dict对象'''
    dict = {}
    dict.update(obj.__dict__)
    return dict
class Preson(object):

    name=""
    age=0
    height=0
    weight=0
    # self类的实例化
    def __init__(self,name,age,height,weight):
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
        
        pass
    def run(self):
        print("run")
    def eat(self,food):
        print("eat"+food)

# 实例化对象
# 格式： 对象名=类名（参数列表）
f=Preson(name="1213",age=12,height=100,weight=100)
# f.name="zzs"
# f.age=22
# f.height=182
# f.weight=99


# f.run()
print(json.dumps(convert_to_dict(f),default=lambda o:o.__dict__,sort_keys=True,indent=4))







