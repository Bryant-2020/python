import re
from collections.abc import Iterable
# match:从头匹配，失败返回None
m1=re.match(r'good','hello world good morning')
print(m1)

#search:搜索整个字符串
# m2=re.search(r'good','hello world good morning')
# print(m2)

#finditer:查找所有匹配数据放到可迭代对象中
# m3=re.finditer(r'x','asxcvsdfghxx')
# for i in m3:
#     print(i)

#findall:把查找到的所有字符串放到列表里
# m4=re.findall(r'x\d+','asx1cvsdfghxx')#'x'+数字
# print(m4)

#fullmatch:完整匹配，字符串需要满足正则规则才有结果
# m5=re.fullmatch(r'hello world','hello world')
# print(m5)

# m=re.search(r'm.*a','fasm ds12m123a456')
# print(m.span())#匹配到字符串的开始结尾下标
# print(m.group())#匹配到的结果
# m=re.search(r'(9.*)(0.*)(5.*7)','dsa9fsf0faa5as7ss')
# print(m.group(1))#可以通过分组名或者编号拿到

#re.compile
# m=re.search(r'm.*a','dsmfsf0faa5as7ss')
# print(m)
# r=re.compile(r'm.*a')
# x=r.search('dsmfsf0faa5as7ss')
# print(x)

#(?P<name>表达式)给分组起名字
# m2=re.search(r'(9.*)(?P<xxx>0.*)(5.*7)','dsa9fsf0faa5as7ss')
# print(m2.groupdict())#{ }字典形式

#正则修饰符
#z=re.findall(r'\w+$','i am a boy\n you are a girl\n he is a man',re.M)
#print(z)
# I：匹配大小写 M：多行匹配 S：使.匹配所有字符

#m=re.search(r'\(.*\)','(456)ads')
#m=re.search(r'f[0-5]m','pdsf4m')匹配多个需要+
#m=re.search(r'f[0-5a-dx]+m','pdsf0axm')#[] 范围
#m=re.search(r'f(x|p|t)m','pdsfxm')# | 只能可选值
#m=re.search(r'f(x|[pr]|t)m','pdsfprm')#加[]只能匹配单个字符
#m=re.search(r'f{2}m','pdsffm')#{n}限定前面字符出现次数

# *	重复零次或更多次
# +	重复一次或更多次
# ?	重复零次或一次
# {n}	重复n次
# {n,}	重复n次或更多次
# {,n}  重复n次或更少次
# {n,m}	重复n到m次

# .	    匹配除换行符以外的任意字符
# \w	匹配字母或数字或下划线或汉字
# \s	匹配任意的空白符
# \d	匹配数字
# \b	匹配单词的开始或结束
# ^	匹配字符串的开始 在[^0-9]z中取反
# $	匹配字符串的结束

# \W	匹配任意不是字母，数字，下划线，汉字的字符
# \S	匹配任意不是空白符的字符
# \D	匹配任意非数字的字符
# \B	匹配不是单词开头或结束的位置

#正则替换：sub
# t='safadfafg'
# m=re.sub(r'a','x',t)
# print(m)

#贪婪模式和非贪婪模式
# *?	重复任意次，但尽可能少重复
# +?	重复1次或更多次，但尽可能少重复
# ??	重复0次或1次，但尽可能少重复
# {n,m}?	重复n到m次，但尽可能少重复
# {n,}?	重复n次以上，但尽可能少重复


# number=input('请输入：')
# if re.fullmatch(r'^\D[a-zA-Z0-9_\-]{3,13}',number):
#     print('y')








