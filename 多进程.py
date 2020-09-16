import multiprocessing
import time
def dance(m):
    for i in range(m):
        time.sleep(0.5)
        print('正在跳舞')

def sing(m):
    for i in range(m):
        time.sleep(0.5)
        print('正在唱歌')

if __name__=='__main__':
    p1=multiprocessing.Process(target=dance,args=(20,))
    p2=multiprocessing.Process(target=sing,args=(20,))
    p1.start()
    p2.start()