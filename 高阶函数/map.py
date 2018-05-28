from  functools import  reduce

# map 功能将传入的幻术依次作用在序列中的每一个元素，并把结果作为新的Iterator（集合）返回
def charint(chr):
    return {"1":1,"2":2,"8":8,"3":3,"4":4,"5":5,"6":6,"7":7}[chr]
list1=["2","5","4"]
# print(charint("1"))

res=map(charint,list1)
print(list(res))


# l=map(str,[1,2,3,4,5])
# print(list(l))

# reduce
# 参数1 为函数
# 参数2 为列表
# 功能:一个函数作用在序列上，这个函数必须接受两个参数，reduce 把结果继续和序列的下一个元素累计运算

# reduce(f,[a,b,c,d])
#f(f(fa,b),c),d)

list2=[1,2,3,4,5]
def add(a,b):
    return a+b
r= reduce(add,list2)
print(r)

def strtoint(str):
    def fc(x,y):
        return x*10+y
    def fs(chr):
        return {"1":1,"2":2,"8":8,"3":3,"4":4,"5":5,"6":6,"7":7}[chr]
    return reduce(fc,map(fs,list(str)))

a=strtoint("3213")
print(a)

