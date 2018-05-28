class Person(object):
    def __init__(self,number):
        self.number=number
    def __add__(self, other):

        return  Person(self.number+other.number)
    def __str__(self):
        return  "number="+str(self.number)

Per1=Person(1)
Per2=Person(2)

print(Per1+Per2)
print(Per1)
print(Per2)
per3=Per1+Per2
print(per3.number)