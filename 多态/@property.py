class Person(object):
    def __init__(self,age):
        self.__age=age
    def getAge(self):
        return  self.__age
    def setAge(self,age):
        if age<0:
            age=0
        self.__age=age

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        if age < 0:
            age = 0
        self.__age = age

per=Person(12)
per.age=-100
print(per.age)