
#装饰器
import time
def cel_time(fn):
    def inner():
        start=time.time()
        fn()
        end=time.time()
    return inner
@cel_time #1.先调用cel_time  2.把被装饰的函数传给fn  demo->fn
def demo():
    print('123')
demo()# 3.再调用demo时，demo函数成了inner函数 demo->inner

def can_play(fn):

    def inner(x,y,*args,**kwargs):
        clock=kwargs['clock']
        #clock=kwargs.get('clock',23)
        if clock<=22:
            fn(x,y)
        else:
            print("it's time to bed")
    return inner
@can_play
def  play_game(name,game):
    print('{}正在玩{}'.format(name,game))

play_game('张三','lol',clock=23)










