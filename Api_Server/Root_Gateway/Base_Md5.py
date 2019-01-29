#Gateway   ,实现生成文件 ，记录信息 ；自动生成sign （每个子类有自己的 params)

import requests ,json ,hashlib ,copy
from Api_Server.Support.Base_Enums import Enums



def MD5(data):
    '''
    返回的字典
    :param data:
    :return:
    '''
    #放在里面要不然签名会失败
    _md5 = hashlib.md5()
    body=json.dumps(data)
    pass_word = body + Enums.password
    _md5.update(pass_word.encode('utf-8'))
    sign = _md5.hexdigest()
    return sign











