def checkPhone(str):
    if len(str)!=11:
        return  False
    elif str[0]!='1':
        return False
    elif str[1:3]!="30"and str[1:3]!="32" and str[1:3]!="33":
        return False
    for i in range(3,11):
        if str[i]<"0"or str[i]>"9":
            return False
    return True
    pass


# print(checkPhone("13322282726"))
import  re

# re.match()
# re.match(pattern 陪陪的正则表达式,string匹配的字符串,flags=0 标志位)
# re.I 忽略大小写
# L 本地户识别
# M 多行匹配
# S 匹配换行符内的所有字符
# U 根据Unicode字符集解析字符
# X 使用我们以更灵活的格式理解正则
# 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话返回NONe

print(re.match("www","www.baidu.com"))
print(re.match("www","www.baidu.com").span())
print(re.match("www","wwW.baidu.com",flags=re.I))
print(re.match("www","baidu.com.www"))


# re.search(pattern 陪陪的正则表达式,string匹配的字符串,flags=0 标志位)
# 扫描整个字符串 并返回第一个成功的匹配

print(re.search("suck","good suck sss  suck "))

# re.findall(pattern 陪陪的正则表达式,string匹配的字符串,flags=0 标志位)
# 扫描整个字符串 并返回列表
print(re.findall("suck","good suck sss  Suck ",flags=re.I))



# 元字符

print("-------------------单个字符与数字-----------------")
# 。匹配换行符以外的任意字符

# print(re.search("[1234567890]","succc  iii  iiss 9"))
# print(re.search("[succcc]","succc  iii  iiss 9"))
# print(re.search("[a-z]","succc  iii  iiss 9"))
# print(re.search("[0-9]","succc  iii  iiss 9"))
# print(re.search("[0-9a-zA-Z]","succc  iii  iiss 9"))
# print(re.search("[0-9a-zA-Z_]","succc  iii  iiss 9"))
# print(re.search("[0-9a-zA-Z_]","succc  iii  iiss 9"))
# # 数字字母下划线
# print(re.search("[^0-9a-zA-Z_]","succc  iii  iiss 9"))
# # 脱字符 除什么之外的
# print(re.search("[\d]","succc  iii  iiss 9"))
# # \d 匹配所有的数字
# print(re.search("[\D]","succc  iii  iiss 9"))
# # \D匹配所有的非数字D
# print(re.search("[\w]","succc  iii  iiss 9"))
# # \匹配数字字母下划线
# print(re.search("[\W]","succc  iii  iiss 9"))
# # \匹配非数字字母下划线'

# print(re.search("[\s]","succ\nc  iii  iiss 9"))
# \匹配任意空白符 \n \f \r \t

# print(re.search("[\]","succ\nc  iii  iiss 9"))
# \匹配非任意空白符 \n \f \r \t


print("-------------- 锚点字符（字符边界）------------------")
# ^行首匹配
# $行尾匹配

print(re.search("^suck","suck  suck  suck  ---"))
print(re.search("suck$","suck  suck  suck  ---"))

# \A 匹配字符串的开始 ，它和^的区别是 \A
print(re.findall("suck","suck  suck \n suck  ---"),re.M)
print(re.findall("\Asuck","suck  suck \n suck  ---"),re.M)
#\Z
print(re.findall("1$","suck  suck 1\n suck  ---1"),re.M)
print(re.findall("1\Z","suck  suck 1\n suck  ---1"),re.M)

# \b 单词边界

print(re.search(r"er\b","never"))

# \B非单词边界
print(re.search(r"er\B","never"))

# x?
print(re.findall(r"er?","neeeerver"))
# x*
print(re.findall(r"er*","neeerverrr"))
# x+
print(re.findall(r"er+","neeerverrr"))
# x(n)确定 n个
print(re.findall(r"e{3}","neeervererr"))
# 至少n个
print(re.findall(r"e{3,}","neeervererr"))
# 至少0到3个e
print(re.findall(r"e{,3}","neeervererr"))
# 3到6个e
print(re.findall(r"e{3,6}","neeeerver333eeeeeereeeeeeeeeeeeeeer"))

print(re.findall("^suck.*man$","suck ssss  man"))


print(re.findall("^suck.*?man$","suck ssss  man"))