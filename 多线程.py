import threading
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('192.168.0.110',9090))
def send_msg():
    while True:
        msg=input('发送内容：')
        s.sendto(msg.encode('utf8'),('192.168.0.110',8080))
        if msg =='exit':
            break
def recv_msg():
    while True:
        data,addr=s.recvfrom(1024)
        print(data,addr)#元组里第一个元素是接收到的数据，第二个是发送发的ip地址和口号
t1=threading.Thread(target=send_msg)#target
t2=threading.Thread(target=recv_msg)
t1.start()
t2.start()


import time
ticket=20
lock=threading.Lock()#创建一把锁
def sell_ticket():
    global ticket
    while True:
        lock.acquire()
        if ticket>0:
            time.sleep(1)
            ticket-=1
            lock.release()
            print('{}卖出一张票，还剩{}张'.format(threading.current_thread().name,ticket))
        else:
            lock.release
            print('售空')
            break
t1=threading.Thread(target=sell_ticket,name='线程1')
t2=threading.Thread(target=sell_ticket,name='线程2')
t1.start()
t2.start()

