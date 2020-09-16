#类方法和静态方法
class Person:
    type='人'
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self,food):
        print(self.name+'正在吃'+food)
    #静态方法：不用到实例对象的任何属性
    #通过类名来调用
    @staticmethod
    def demo():
        print('hello')
    #类方法：只用到类属性
    #使用实例对象和类对象调用
    @classmethod
    #cls指类对象，通过类对象访问类属性
    def test(cls):
        print(cls.type)
p1=Person('张三',18)
p1.eat('红烧牛肉')#实例对象调用方法，(对象名.方法名(参数))
Person.eat(p1,'西红柿')#类对象名调用方法，手动传参
p1.demo()
p1.test()


#私有变量的定义和获取
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.__money = 2000 # __money 是私有变量，外部无法访问
    def get_money(self): # 定义了get_money ⽅法，在这个方法⾥获取到 __money
        return self.__money # 内部可以访问 __money 变量
    def set_money(self,money): # 定义了set_money ⽅法，在这个方法⾥，可以修改 __money
        self.__money = money
p = Person('王五',21)
# 外部通过调用 get_money 和 set_money 这两个公开方法获取和修改私有变量
print(p.get_money())
p.set_money(8000)
print(p.get_money())
#print(p._Ptudent__money)#获取私有变量方法：对象._类名__私有变量名


#单例类
class Singleton(object):
    __instance = None#类属性，实例为空
    __is_first = True
    #new方法：申请内存
    def __new__(cls, age, name):
        if  cls.__instance is None:
            cls.__instance = object.__new__(cls)#创建实列对象
        return cls.__instance
    def __init__(self, age, name):
        if self. __is_first: # 不会再创建第二个对象
            self.age = age
            self.name = name
            Singleton. __is_first = False
a = Singleton(18, "张三")
b = Singleton(28, "李四")
print(id(a))
print(id(b))
print(a.age) # 18
print(b.age) # 18
a.age = 19
print(b.age)