import  random
# import numpy as np


class Preson(object):

    def __init__(self,hp,mp,qiang):
        self.Hp=hp
        self.__Mp=mp
        self.qaing=qiang
    def sMp(self):
        print(self.__Mp)
    def setMp(self,mp):
        self.__Mp=mp
    def getMp(self):
        return self.__Mp
    def kaiqiang(self,one):
        one.Hp-=self.qaing.kill

        return  one




class Ak(object):
    kill=43
    def __init__(self):
        pass

class M16(object):
    kill=34
    def __init__(self):
        pass
oneqiang=Ak()


class Man(Preson):
    def __init__(self,hp,mp,qiang,sex):
        super(Man, self).__init__(hp,mp,qiang)
        self.sex=sex


man = Man(1000, 100, oneqiang,"man")
man.setMp(10000)
print(man.getMp(), man.sex)
class worker(Man):
    def __init__(self,hp,mp,qiang,sex,work):
        super(worker,self).__init__(hp,mp,qiang,sex)
        self.work=work

worker1=worker(100,10,oneqiang,"man","It")
print(worker1.work)
# one=Preson(1000,100,oneqiang)
# # one.__Mp=100
# one.sMp()
# one.__Mp=1000
# one.setMp(1000)

# twoqiang=M16()
# two=Preson(1000,100,twoqiang)


# one.kaiqiang(two)
# print np.random.rand(4,4)

# while one.Hp>0 and two.Hp>0:
#     a=random.randint(1,100)
#     if a>two.qaing.kill:
#         one = two.kaiqiang(one)
#         print("one=%d two=%d" % (one.Hp, two.Hp))
#     else:
#         two = one.kaiqiang(two)
#         print("one=%d two=%d" % (one.Hp, two.Hp))
#
#
#
#     if one.Hp<0:
#         print("two  win")
#     if two.Hp<0:
#         print("One  win")
#     pass

