# 排序

list=[1,2,5,3,3,4532,5,2,3,6,432,5,23,333]

list2=sorted(list)

print(list2)

list3=[1,2,5,-3,3,-4532,5,2,3,-6,432,5,23,333]
# 绝对值
list4=sorted(list3,key=abs)
print(sorted(list3))
print(list4)


# 降序
list5=[1,2,5,3,3,4532,5,2,3,6,432,5,23,333]
list6=sorted(list5,reverse=True)
print(list6)

# 自定义条件
liststr=["fdasfas","fsd","fsdfsdfsadfas"]
def mylen(str):
    return len(str)
lit8=sorted(liststr,key=mylen)
print(lit8)
