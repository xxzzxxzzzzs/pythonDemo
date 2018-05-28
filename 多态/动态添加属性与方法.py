from  types import MethodType
class Person(object):
    # 限制添加
    __slots__ = ("name","speak")
    pass

per=Person();

per.name="tom"
print(per.name)

def say(self,name):
    print("say"+name)
#     动态添加参数
per.speak=MethodType(say,per)
per.speak(per.name)