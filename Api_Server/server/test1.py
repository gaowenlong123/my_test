import threading
from time import ctime,sleep


def music(func):
    for i in range(2):
        print("I was listening to %s. %s" %(func,ctime()))
        sleep(1)

def move(func):
    for i in range(2):
        print("I was at the %s! %s" %(func,ctime()))
        sleep(5)



# 1

# threads = []
# t1 = threading.Thread(target=music,args=(u'爱情买卖',))
# threads.append(t1)
# t2 = threading.Thread(target=move,args=(u'阿凡达',))
# threads.append(t2)
#
# if __name__ == '__main__':
#     for t in threads:
#         #setDaemon(True)将线程声明为守护线程，必须在start() 方法调用之前设置 。设置之后主线程停止了，子线程也可以运行下去
#         # 如果不设置为守护线程程序会被无限挂起,然后子线程启动后，父线程也继续执行下去，当父线程执行完最后一条语句print "all over %s" %ctime()后，没有等待子线程，直接就退出了，同时子线程也一同结束。
#         t.setDaemon(True)
#         t.start()
#
#         # join（）的作用是，在子线程完成运行之前，这个子线程的父线程将一直被阻塞。
#         # join()方法的位置是在for循环外的，也就是说必须等待for循环里的两个进程都结束后，才去执行主进程。
#     t.join()
#
#     print("all over %s" %ctime())


#  ===> 2   一个一个调不方便,故修改一下  做一个方法来分发，根据输入执行 for循环 。。。。
# def player(name):
#     r = name.split('.')[1]
#     if r == 'mp3':
#         music(name)
#     else:
#         if r == 'mp4':
#             move(name)
#         else:
#             print('error: The format is not recognized!')
#
# list = ['爱情买卖.mp3','阿凡达.mp4']
#
# threads = []
# files = range(len(list))
#
# #创建线程
# for i in files:
#     t = threading.Thread(target=player,args=(list[i],))
#     threads.append(t)



# 3===》  把想要播放的方法做了优化
def super_player(file,time):
    for i in range(2):
        print('Start playing： %s! %s' %(file,ctime()))
        sleep(time)

#播放的文件与播放时长
list = {'爱情买卖.mp3':3,'阿凡达.mp4':5,'我和你.mp3':4}

threads = []
files = range(len(list))

#创建线程
for file,time in list.items():
    t = threading.Thread(target=super_player,args=(file,time))
    threads.append(t)


if __name__ == '__main__':
    #启动线程
    for i in files:
        threads[i].start()
    for m in files:
        threads[m].join()
    #主线程
    print('end:%s' %ctime())