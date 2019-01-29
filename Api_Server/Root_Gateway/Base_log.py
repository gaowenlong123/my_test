
def error_log(str):
    print(bcolor.FAIL + str + bcolor.ENDC)
    print(str)
    # print("\033[31m"+str+"\033[0m")

def green_log(str):
    print("\033[32m" + str + "\033[0m")

def yellow_log(str):
    print("\033[33m" + str + "\033[0m")

def blue_log(str):
    print("\033[34m" + str + "\033[0m")

def start_log(isStart=True):
    str = "开始测试" if isStart else "结束测试"
    print("\033[5;34;46m","**"*10,str,"**"*10,"\033[0m")

class bcolor(object):
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'



if __name__ == '__main__':
    error_log("1")
    yellow_log("1")
    blue_log("1")
    green_log("2")

    print(bcolor.WARNING + 'WARNING: start httpd failed' + bcolor.ENDC)
    print(bcolor.OKGREEN + 'starting......' + bcolor.ENDC)
    print(bcolor.OKBLUE + 'starting......' + bcolor.ENDC)
    print(bcolor.FAIL + 'starting......' + bcolor.ENDC)
    print(bcolor.HEADER + 'starting......' + bcolor.ENDC)
