#全局变量和局部变量
a=10
def test():
    global a #修改全局变量
    a=20
    print('函数内部a={}'.format(a))#20
test()
print('函数外部a={}'.format(a))#20

#返回多个值 return x,y 本质是元组
def function(a, b, *args, mul=1,**kwargs):
    print(function(9,5,8,2,0,p=9,q=10))
#a=9,b=5,
# *args:可变参数  多余的可变参数以元组形式保存 *args=(8,2,0）
# mul :缺省参数 mul=1,
# **kwargs:可变的关键字参数  多余的以字典形式保存**kwargs:{p:9,q:10}