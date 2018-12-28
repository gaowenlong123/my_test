def list_ToString(list ,inser=','):
    _str=''
    for i in list:
        _str+=str(i)+inser
    return _str[0:-1]

if __name__ == '__main__':
    list_ToString([6,13])
