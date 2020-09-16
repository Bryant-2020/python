class Student():
    __slot__=('name','age','city')
    #定义在类里，元组形式，规定对象可以存在的属性
    #只对当前类作用
    def __init__(self,name,age):
        self.name=name#赋值
        self.age=age
    def say_hello(self):
        print('大家好，我是{},我{}岁'.format(self.name,self.age))
    def __del__(self):#代码销毁后自动调用
        print('此函数被调用')
    def __str__(self):#print打印对象时调用此方法
        return '443'
    def __call__(self, *args, **kwargs):
        print('__call__')
s=Student('张三',18)
print(s.name)
s.say_hello()
s.city='上海'#添加属性
print(s.city)
print(s)
s()#触发__call__

#
class Student():
    '''
    学生系统
    '''
    def __init__(self,name,age):
        self.name=name#赋值
        self.age=age
    def __eq__(self,other):
        return self.name==other.name and self.age==other.age
s1=Student('张三',18)
s2=Student('lisi',17)
print(s1==s2)#调用__eq__比较所有的值
print(s1.__doc__) #类的说明
print(s1.__dict__)#字典形式输出属性和方法
print(s1.__class__)#当前类
print(s1.__module__)#当前模块