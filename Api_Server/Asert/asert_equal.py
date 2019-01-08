#仅适配gateway
'''
做判断就是做判断， 以校验为导向：  实现接口 - 处理数据 - 对比数据 - 断言 - 打印其他数据
'''

from Api_Server.Support.Base_Compare import *
from Api_Server.Decorate_Data.Extract_Value_Tostring import *

#只做校验
def asert_equal(data,key ,targrt):
    '''
    接口有数据存在，且不重复
    :param data:
    :param key:
    :param targrt:
    :return:
    '''

    if data[key]==targrt:
        return {"result": True, "msg": str(data[key]) + " 等于 "+ str(targrt)}
    else:
        return {"result": False, "msg": str(data[key]) + " 不等于 "+ str(targrt)}

    # for _dict in data:
    #     result=map(_dict ,key ,default="无")
    #
    #     if targrt == result:
    #         keyValues_ToString(_dict ,key_list=[key ,"title"])
    #
    #     else:
    #         continue
    #
    # #判断
    # if len(isTrue) == 1:
    #     print("接口正确")
    # elif len(isTrue) > 1 :
    #     print("接口数据有重复 ,或请检查校验的Key值")
    # else:
    #     print("接口无该数据")


def asert_equal_ByIndex(data, key ,by_index, targrt=''):
    '''
    接口有数据存在，且不重复
    :param data:
    :param key:
    :param targrt:
    :return:
    '''
    isTrue = []
    for index, _dict in enumerate(data):
        if index + 1 not in by_index:
            continue
        result = map(_dict, key, default="无")

        if targrt == result:
            print('第' + str(index + 1) + '行：', end='')
            keyValues_ToString(_dict, key_list=[key, "title"])
            isTrue.append(1)
        else:
            continue

    # 判断
    if len(isTrue) == 1:
        print("接口正确")
    elif len(isTrue) > 1:
        print("接口数据有重复 ,或请检查校验的Key值")
    else:
        print("接口无该数据")


#同时做接口性能的校验
def i_asert_equal(func ,key ,):
    while(True):
        _data = func()

    #请求五十次，数据依然存在接口中
    #2 接口多长时间才会相应，数据存在接口中


