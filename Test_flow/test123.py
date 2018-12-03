import time
for i in range(100):
    print('dd' + time.strftime('%Y.%m.%d', time.localtime(time.time())))