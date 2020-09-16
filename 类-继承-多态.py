class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Student(Person):
    def __init__(self, name, age, score):
        super().__init__(name, age)
        self.score = score
class Dog():
    def __init__(self, name, color):
        self.name = name
        self.color = color
p = Person('tony', 18)
s = Student('jack', 20, 90)
d = Dog('旺财', '白色')
print(isinstance(p, Person)) # True.对象p是由Person类创建出来的
print(isinstance(s, Person)) # True.对象s是有Person类的子类创建出来的
print(isinstance(d, Person)) # False.对象d和Person类没有关系
print(issubclass(Student, Person)) # True
print(issubclass(Dog, Person))

#多态的使用
class Dog():
    def work(self):
        print('正在工作')
class PoliceDog(Dog):
    def work(self):
        print('正在搜捕')
class BlindDog(Dog):
    pass
class Person():
    def __init__(self,name,dog):
        self.name=name
        self.dog=dog
    def work_with_dog(self):
        self.dog.work()
p=Person('李四',Dog())
p.work_with_dog()
B=Person('李四',PoliceDog())
B.work_with_dog()


class Point():
    def __init__(self,x:int,y:int):
        self.x=x
        self.y=y
class Rectangle():
    def __init__(self,top_left:Point,bottom_right:Point):
        self.top_left=top_left
        self.bottom_rght=bottom_right
    def judge(self,point):
        if self.top_left.x <point.x<self.bottom_rght.x \
            and self.bottom_rght.y<point.y<self.top_left.y :
            print('在矩形内')
        else:
            print('不在矩形内')
p=Point(2,10)
p1=Point(0,5)
p2=Point(5,0)
r=Rectangle(p1,p2)
r.judge(p)

class Student():
    def __init__(self,number,name,age,gender,score):
        self.number=number
        self.name=name
        self.age=age
        self.gender=gender
        self.score=score
    def __str__(self):
         return '学号:{},姓名:{},年龄:{},性别:{},分数:{}'.format(self.number,self.name,self.age,self.gender,self.score)
class Grade():
    def __init__(self,grade_name,student_list):
        self.grade_name=grade_name
        self.student_list=student_list

    def show(self):
        for student in self.student_list:
            print(student)

    def fail_students(self):
        result=filter(lambda student : student.score<60 ,self.student_list)
        for x in result:
            print('不及格的学生:',x)

    def search(self):
        x=int(input('输入要查找的学号:'))
        for student in self.student_list:
            if student.number==x:
                return student
        else:
            return '不存在'
s1=Student(1,'zhangsan',18,'male',80)
s2=Student(6,'zhangsi',17,'fmale',100)
s3=Student(7,'wangsan',18,'male',99)
s4=Student(9,'wangsi',19,'fmale',55)
s5=Student(8,'hangsan',18,'male',88)
a=Grade('三班',[s1,s2,s3,s4,s5]) #对象a
a.show()
a.fail_students()
print(a.search())

