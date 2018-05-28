lit=[1,2,3,4,5,6,7,8]

def fun(num):
    if num%2==0:
        return  True
    return False


l= filter(fun,lit)

print(list(l))

data=[["姓名","年龄","爱好"],["tom",25,"no"],["zz",42,"aaa"],["dasd",32,"no"]]
def func2(v):
    v=str(v)
    if v=="no":
        return False
    return True

for line in data:
    m=filter(func2,line)
    print(list(m))


data2=[{"name":"tom","age":"25"},{"name":"tom","age":"25"},{"name":"tom","age":"25"},{"name":"ss","age":"53"},{"name":"zzss","age":"21"}]

def older(man):
    if int(man['age'])>22:
        return True
    return False
dataOder=filter(older,data2)
print(list(dataOder))