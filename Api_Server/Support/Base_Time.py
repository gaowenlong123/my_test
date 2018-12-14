import time

def get_time():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))



def time_Stamp():
    _time = get_time()
    temp=time.strptime(_time ,'%Y-%m-%d %H:%M:%S' )
    return int(time.mktime(temp))








