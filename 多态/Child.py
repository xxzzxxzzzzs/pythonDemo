from Man import man
from WoMan import woman

class Child(man,woman):
    def __init__(self,sex,say,buy):
        man.__init__(self,sex)
        woman.__init__(self,say)
        self.buy=buy

c=Child("man","ssss","ams")
print(c.buy)