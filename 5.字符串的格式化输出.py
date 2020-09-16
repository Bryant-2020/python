print('我是%d号' % 5)
print('我是%3d号' % 5)
print('我是%03d号' % 5)
print('我是%-3d号' % 5)

d=['张山',18,'shanghai',180]
b='大家好，我是{},我今年{},我来自{},身高{}cm'.format(*d)#列表用
print(b)

a=[1,5,6,8,9,2,4,3,6]
print(a.index(6)) #2
print(a.count(6))#2
a=[1,5,6,8,9,2,4,3,6]
print(a[::-1])  [6, 3, 4, 2, 9, 8, 6, 5, 1]

x=[1,2,3]
y=x  #这里x和y用的同一个地址,会互相影响
z=x.copy() # z和x地址不同
[[0]*3]#[[0, 0, 0]]

m=[i for i in range(1,101)]
print(m)
n=[m[j:j+3] for j in range(0,100,3)]
print(n)
print('-'.join(['a','p','p','l','e'])) #a-p-p-l-e


str='how are you and you?'
a=str.split('you')#['how are ', ' and ', '?']
print(a)
b='me'.join(a)# how are me and me?
print(b)
print('xxx.txt'.rpartition('.'))#从右边切('xx.x', '.', 'txt')
print('xxx.txt'.partition('.'))#从左边切('xx', '.', 'xx.txt')
eval()#字符串的操作加减乘除

data='GET /register HTTP/1.1'
path=data.splitlines()[0].split(' ')[1]
print(path)

