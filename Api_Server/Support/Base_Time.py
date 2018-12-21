import time

def get_time():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))



def time_Stamp():
    _time = get_time()
    temp=time.strptime(_time ,'%Y-%m-%d %H:%M:%S' )
    return int(time.mktime(temp))


def get_late_time(times=0):
    _time = get_time()
    temp = time.strptime(_time, '%Y-%m-%d %H:%M:%S')
    temp=int(time.mktime(temp))
    totle=temp+60*times
    timeArray = time.localtime(totle)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime






