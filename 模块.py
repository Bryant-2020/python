#导入系统模块
# import random
# from random import randint
# from math import * #导入模块里所有方法和变量
# import datetime as dt

import os
# print(os.getcwd())
# print(os.name) #windos->nt, other->posix
# os.mkdir('name') 创建文件夹
#os.rmdir('name')  删除文件夹
#os.listdir
# os.sep #分隔符 \ , /
# os.path.abspath #->文件绝对路径
# os.path.isdir# 判断是否是文件夹
# os.path.isfile# 判断是否是文件
# os.path.splitext(file_name)

# import random
# print(random.random())  [0,1) float
# print(random.uniform(20,30)) [20,30] float
# print(random.randint(10,30)) [10,30] int
# print(random.randrange(20,30)) [20,30) int
# print(random.choice('abcdefg'))
# print(random.sample('abcdefg',3))

# import hashlib
# import hmac
# x=hashlib.md5('abc'.encode(encoding='utf8'))
# print(x.hexdigest()) 16进制
# h2=hashlib.sha224('123456'.encode())#224/56
# h3=hac.new('123'.encode)

# 使用自定义模块
# import module
# module.function()
# from module import * 本质查找__all__属性,只调用all属性内的
# x='1'
# y='2'
# def foo():
#     print('123')
# __all__=('x','foo')

#if __name__=='__main__': 只有直接运行当前py文件才行

