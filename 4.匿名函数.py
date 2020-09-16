#lambda 匿名函数可以是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
max=lambda x,y:x<y
print(max(5,1))

students=[{'name':'wang','age':24,'score':100},
{'name':'li','age':62,'score':78},
{'name':'he','age':86,'score':22},
{'name':'fe','age':22,'score':66}]
students.sort(key=lambda ele: ele['age'])
print(students)
b=sorted(students,key=lambda ele: ele['age'])
print(b)

#filter 内置类的使用:过滤
ages=[22,33,24,95,20]
x=list(filter(lambda ele : ele>18 ,ages))

#map 映射函数内所有数据
ages=[22,33,24,95,20]
x=list(map(lambda ele : ele+1 ,ages))

# reduce 把前两个元素（只能两个）传给函数，函数加工后，
# 然后把得到的结果和第三个元素作为两个参数传给函数参数，依次类推。
from functools import reduce
students=[{'name':'wang','age':24,'score':100},
            {'name':'li','age':62,'score':78},
            {'name':'he','age':86,'score':22},
            {'name':'fe','age':22,'score':66},
            {'name':'ti','age':55,'score':44} ]
print(reduce(lambda x,y:x+y['age'],students,0))

