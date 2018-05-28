import  unittest

from  单元测试 import mysum
from  单元测试 import mysbu
class Test(unittest.TestCase):
    def setUP(self):
        print("开始测试自动调用")
    def tearDown(self):
        print("结束测试自动调用")

    def test_mysum(self):
        self.assertEqual(mysum(1,2),3,"加有错")
    def test_mysbu(self):
        self.assertEqual(mysbu(1,2),-1,"减有错")
if __name__ =="__main__":
    unittest.main()