import itertools
# mylist=list(itertools.permutations("1234567890",6))
# print(mylist)
# print(mylist.__len__())

mylist2=list(itertools.product("1234567890",repeat=4))
print(mylist2)
print(mylist2.__len__())