class House():
    def __init__(self,house_type,total_area,fru_list=None):
        if fru_list is None:#可变参数
            fru_list=[]
        self.house_type=house_type
        self.total_area=total_area
        self.free_area=total_area*0.6
        self.fru_list=fru_list
    def add(self,x):
        if x.area<3:
            self.fru_list.append(x.name)
    def __str__(self):
        return '可安置家具列表={}'.format(self.fru_list)
class Furniture():
    def __init__(self,name,area):
        self.name=name
        self.area=area
house=House('两室一厅',100)
bed=Furniture('床',4)#每个对象都占据内存空间
chest=Furniture('衣柜',2)
table=Furniture('餐桌',1)
house.add(bed)
house.add(chest)
house.add(table)
print(house)


from abc import ABCMeta, abstractmethod
class Employee(metaclass=ABCMeta):
    """员工(抽象类)"""
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        """结算月薪(抽象方法)"""
        pass

class Manager(Employee):
    """部门经理"""
    def get_salary(self):
        return 15000.0

class Programmer(Employee):
    """程序员"""
    def __init__(self, name, working_hour=0):
        self.working_hour = working_hour
        super().__init__(name)
    def get_salary(self):
        return 200.0 * self.working_hour

class Salesman(Employee):
    """销售员"""
    def __init__(self, name, sales=0.0):
        self.sales = sales
        super().__init__(name)
    def get_salary(self):
        return 1800.0 + self.sales * 0.05

class EmployeeFactory:
    """创建员工的工厂（工厂模式 - 通过工厂实现对象使用者和对象之间的解耦合）"""

    @staticmethod
    def create(emp_type, *args, **kwargs):
        """创建员工"""
        all_emp_types = {'M': Manager, 'P': Programmer, 'S': Salesman}
        cls = all_emp_types[emp_type.upper()]
        return cls(*args, **kwargs) if cls else None

def main():
    """主函数"""
    emps = [
        EmployeeFactory.create('M', '曹操'),
        EmployeeFactory.create('P', '荀彧', 120),
        EmployeeFactory.create('P', '郭嘉', 85),
        EmployeeFactory.create('S', '典韦', 123000),
    ]
    for emp in emps:
        print(f'{emp.name}: {emp.get_salary():.2f}元')

if __name__ == '__main__':
    main()