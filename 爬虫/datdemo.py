path=r"C:\Users\Administrator\Desktop\投资经理编程题所需数据\编程题数据\逐笔成交\001.dat"

# def read_bigFile():
#     f = open(path,'r',encoding="")
#     cont = f.read(10)
#     while len(cont) >0 :
#         print(cont)
#         cont = f.read(10)
#     f.close()
# read_bigFile()

with open(path, 'rb') as fp:
    data = fp.read()      #type(data) === bytes
    text = int.from_bytes(data, byteorder='big')
    print(data)
fp.close()