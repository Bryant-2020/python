#相对路径：
# ../ 表示返回到上一级文件夹
# r :只读，
# w:只写，并且会覆盖之前操作，
# a:追加模式，追加内容，创建文件
import json
filename='C:/Users/Administrator/Desktop/数据表.txt'
# #filename=r'C:\Users\Administrator\Desktop\数据表.txt'
file='test.txt'
new_file=open(file,'w')
try:
    with open(filename,'r',encoding='utf8') as file_object:
        while True:
            content=file_object.readline().strip(',\n')
            json.dump(content,new_file)
            if not content:
                break
except FileExistsError:
    print("文件不存在")



# while True:
#     content=file_object.readline()
#     print(content)
#     if content =='':
#         break
#x=file_object.readlines()#列表形式读取
#print(x)

# import os
# file_name='C:/Users/Administrator/Desktop/数据表.txt'
# if not os.path.isfile(file_name):
#     print("文件不存在")
# else:
#     old_file=open(file_name)
#     new='test.txt'
#     print(new.rpartition('.'))
#     new_file=open(new,'w')
#     new_file.write(old_file.read())
#     new_file.close()
#     old_file.close()

#序列化：将数据从内存持久化保存到硬盘
#反序列化：将数据从硬盘加载到内存的过程
#write方法只能写字符串或者二进制
#json模块转换成字符串或者pickle模块转换成二进制
#import json
# names=['a','s','d','f']
# filename='numbers.txt'
# with open(filename,'w') as file:
#     json.dump(names,file)#转换并存储
#     #x=json.dumps(names)#只转换

# filename='numbers.txt'
# with open(filename) as file:
#     names=json.load(file)
# print(names)

