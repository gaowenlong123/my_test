from Api_Repository.Interface.App.channel.channel_V8_2.I_channel_V8_2 import I_channel_V8_1
from Api_Server.Support.Base_APP import *



def a():
    i = I_channel_V8_1(channel_type.video)
    print(i.feed(1))


threads = []

import threading ,time
#创建线程
for m in range(3):
    t = threading.Thread(target=a,)
    threads.append(t)
    time.sleep(2)

if __name__ == '__main__':
    #启动线程
    # a()
    for m in range(3):
        threads[m].start()
    for m in range(3):
        threads[m].join()