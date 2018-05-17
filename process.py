import multiprocessing
from time import sleep, ctime

def super_player(file_, time):
    for i in range(2):
        print('Start playing: %s! %s' % (file_, ctime()))
        sleep(time)


lists = {'summer.mp3': 3, 'afanda.mp4': 5, '因为爱情': 4}
threads = []
files = range(len(lists))

for file_, time in lists.items():
    t = multiprocessing.Process(target=super_player,args=(file_,time))
    threads.append(t)
if __name__ == '__main__':
    for i in files:
        threads[i].start()
    for i in files:
        threads[i].join()
    print('end:%s' % ctime())