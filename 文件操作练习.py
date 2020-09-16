user_list=[]
def add_user():
    name=input('请输入姓名:')
    tel=input('请输入手机号:')
    qq=input('请输入QQ号:')
    user={'name':name,'tel':tel,'qq':qq}
    user_list.append(user)
    print(user_list)
def del_user():
    name=input('请输入要删除的用户名:')
    for u in user_list:
        if u['name']==name:
            user_list.remove(u)
            print('删除成功')
        else:
            print('用户不存在')
def modify_user():
    name=input('请输入要修改的用户名:')
    for u in user_list:
        if u['name']==name:
            print('您想修改的信息是:\n姓名:{name},手机号:{tel},QQ号:{qq}'.format(**u))
            u['name']==input('请输入新的姓名:')
            u['tel']=input('请输入新的手机号:')
            u['qq']=input('请输入新的QQ号:')
        else:
            print('用户不存在')
def search_user():
    name=input('请输入要查找的用户名:')
    for u in user_list:
        if u['name']==name:
            print('查询信息是:\n姓名:{name},手机号:{tel},QQ号:{qq}'.format(**u))
        else:
            print('用户不存在')
def show_all():
    print('姓名     手机号        QQ号')
    for u in user_list:
        print(u['name'],u['tel'].center(15),u['qq'].center(15))
def exit_system():
    answer=input('确定请输入Y,返回上一层请输入R：\n')
    if answer.upper()=='Y':
        exit()
    elif answer.upper=='R':
        start()
def start():
    while True:
        print(
            '----------------\n名片管理系统 v1.0\n'
            '1：添加名片\n2：删除名片\n3：修改名片\n4：查询名片\n5：显示所有用户\n6：退出系统\n-----------')
        number=input('请选择对应操作(数字):')
        if number=='1':
            add_user()
        elif number=='2':
            del_user()
        elif number=='3':
            modify_user()
        elif number=='4':
            search_user()
        elif number=='5':
            show_all()
        elif number=='6':
            exit_system()
        else:
            print('输入有误，请重新输入')
if __name__=='__main__':
    start()

