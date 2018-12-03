#把字典数据写进临时文件中
import pickle
from Base.Base.Base_File import remove_file
import os

def write(data, path="data.pickle"):           #直接替换
    with open(path, 'wb') as f:
        pickle.dump(data, f, 0)


def read(path='data.pickle' , is_clear=False):                #读取全部
    data = {}
    with open(path, 'rb') as f:
        try:
            data = pickle.load(f)
        except EOFError:
            data = {}
            print("Error ====> 文件为空")
    if is_clear:
        remove_file('data.pickle')
    return data


def writeInfo(data, path="data.pickle"):

    _read = read(path)
    result = {}
    if _read:
        _read.update(data)
        result = _read
    else:
        result.update(data)
    with open(path, 'wb') as f:

        pickle.dump(result, f)

if __name__ == "__main__":
    # write({})  #生成文件
    writeInfo({'112344':1223})       #写一个数据
    a=read(is_clear=True)             #读数据，删除临时文件
    print(a)                            #{'112344': 1223}
