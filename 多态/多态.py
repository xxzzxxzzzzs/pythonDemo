

class Animal(object):
    def __init__(self,name):
        self.name=name
    def eat(self):
        print(self.name,"eat")

class Cat(Animal):
    def __init__(self,name):
       super(Cat,self).__init__(name)

class Dog(Animal):
    def __init__(self,name):
       super(Dog,self).__init__(name)

class Person(object):
    __slots__ = ("name","age")
    def __init__(self):
        pass
    # def feedCat(self,cat):
    #     print("feed")
    #     cat.eat();
    # def feedDog(self,dog):
    #     print("feed")
    #     dog.eat()
    def feedAnimal(self,animal):
        print("feed")
        animal.eat()

tom=Cat("tom")
jk=Dog("Jk")
joj=Person()
joj.name="dsada"
joj.sex="man"
joj.feedAnimal(tom)