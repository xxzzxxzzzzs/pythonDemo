# -*- coding: UTF-8 -*-
def prit(number):
    # assert (number >0),"大于0"
    try:
        print(1 / number)
    except BaseException as e:

        print("有问题")
    finally:
        print("最终执行")
    return


print(prit(1))
print(prit(1))