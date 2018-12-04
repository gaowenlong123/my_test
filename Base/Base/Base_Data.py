#运行时候 先用Pickle ，结束时输出到text

def write_init(path='b.text'):
    data = '接口统计   只存一次运行\n'
    with open(path, 'w+') as f:
        f.write(data)


def write(data, path):           #累加
    all = read(path)
    data+='\n'
    all+=data
    with open(path, 'w+') as f:
        f.write(all)



def read(path ):                #读数据
    with open(path, 'r+') as f:
        data=f.read()
    f.close()
    return data






if __name__ == '__main__':
    write_init()
    a=read('b.text')
    write('aaccccccccccc','b.text')