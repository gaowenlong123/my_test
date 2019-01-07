#  只修饰数据   ，例如键值对生成字符串

def list_ToString(list ,inser=','):
    #将字典里的 值 输出成字符串
    _str=''
    for i in list:
        _str+=str(i)+inser
    return _str[0:-1]

if __name__ == '__main__':
    list_ToString([6,13])
