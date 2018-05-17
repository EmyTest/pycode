import threading
from time import sleep,ctime

#创建线程类
class MyThread(threading.Thread):
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name
    def run(self):

        self.func(*self.args)
def super_play(file_,time):
    for i in range(2):
        print('Start playing: %s! %s'%(file_,ctime()))
        sleep(time)
lists = {'summer.mp3':3,'afanda.mp4':5,'因为爱情':4}
threads = []
files = range(len(lists))

for file_,time in lists.items():
    t = MyThread(super_play,(file_,time),super_play.__name__)
    threads.append(t)
if __name__=='__main__':
    for i in files:
        threads[i].start()
    for i in files:
        threads[i].join()
    print('end:%s'%ctime())