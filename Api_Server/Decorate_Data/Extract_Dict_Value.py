#  路径sting  拿出字典中对应的值
from Api_Server.Decorate_Data.Check_Response_Data import *


def get_dict_value(dict ,template_path='data/items'):
    '''

    :param dict:
    :param template_path:
    :return:                  {'_isSuccess': True, '_msg': '接口请求成功', 'data': data}
    '''
    re_dict=check_request(data=dict)
    if re_dict["_isSuccess"] == False:
        return re_dict
    temp_list = template_path.split('/')
    for key in temp_list:
        dict = dict[key]
    re_dict["data"]=dict
    return re_dict