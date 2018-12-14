#运行时候 先用Pickle ，结束时输出到text         垃圾 ，不好用，就不用你了

def write_text_init(path='b.text'):
    data = '接口统计   只存一次运行\n'
    with open(path, 'w+') as f:
        f.write(data)

def write_text_add(data,path='b.text'):

    with open(path, 'w') as f:
        f.write(data)

def write_text(data, path):           #累加
    all = read_text(path)
    data+='\n'
    all+=data
    with open(path, 'w+') as f:
        f.write(all)



def read_text(path ):                #读数据
    with open(path, 'r+') as f:
        data=f.read()
    f.close()
    return data

def read_text_by_gbk(path ):                #读数据
    with open(path, mode='rb') as f:
        data=f.read()
    f.close()
    return data





if __name__ == '__main__':
    a=read_text('b.text')
    write_text('aaccccccccccc','b.text')