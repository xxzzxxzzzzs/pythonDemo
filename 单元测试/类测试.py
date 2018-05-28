# from  Person import Person
#
# per=Person("tom",24)
#
# print(str(per.getName()))

import unittest
from  Person import Person
class Test(unittest.TestCase):
    def test_init(self):
        p=Person("tome",22)
        self.assertEqual(p.name,"tome","error")


if __name__ =="__main__":
    unittest.main()
    