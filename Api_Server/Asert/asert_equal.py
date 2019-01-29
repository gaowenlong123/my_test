from Api_Server.Support.Base_Compare import *
from Api_Server.Decorate_Data.Extract_Value_Tostring import *


def asert_equal(data,key ,targrt):
    '''
    只做校验 ， 接口有数据存在，且不重复
    例： _data的“state”是否为“offline”
    :param data:_data
    :param key:"state"
    :param targrt:"offline"
    :return:
    '''

    if data["_isSuccess"] == False:
        return {"result":False ,"msg":data["msg"]}

    if data.get(key , None) == None:
        temp = map_List_dict(data ,key ,None)
    else:
        temp = data[key]

    if temp==targrt:
        return {"result": True, "msg": str(temp) + " 等于 "+ str(targrt)}
    else:
        return {"result": False, "msg": str(temp) + " 不等于 "+ str(targrt)}




    # 接口性能的校验
def asert_capability(func, key, ):
    pass





# def asert_equal_ByIndex(data, key ,by_index, targrt=''):
#     '''
#     接口有数据存在，且不重复
#     :param data:
#     :param key:
#     :param targrt:
#     :return:
#     '''
#     isTrue = []
#     for index, _dict in enumerate(data):
#         if index + 1 not in by_index:
#             continue
#         result = map(_dict, key, default="无")
#
#         if targrt == result:
#             print('第' + str(index + 1) + '行：', end='')
#             keyValues_ToString(_dict, key_list=[key, "title"])
#             isTrue.append(1)
#         else:
#             continue
#
#     # 判断
#     if len(isTrue) == 1:
#         print("接口正确")
#     elif len(isTrue) > 1:
#         print("接口数据有重复 ,或请检查校验的Key值")
#     else:
#         print("接口无该数据")






