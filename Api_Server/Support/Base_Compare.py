import random
def map(dict, objkey, default='default'):
    '''
    # 获取字典中的objkey对应的值，适用于字典嵌套
    :param dict: 字典
    :param objkey: 目标key
    :param default: 找不到时返回的默认值
    :return:
    '''
    tmp = dict
    for k, v in tmp.items():
        if k == objkey:
            return v
        else:
            if type(v) is type({}):
                ret = map(v, objkey, default)
                if ret is not default:
                    return ret
    return default

def get_random_value(dict ,key ,nums=1):
    '''
    :param dict:
    :param key:  值是一个list
    :param nums:
    :return:
    '''
    re_list=[]
    _list = []
    _num = len(dict[key])-1
    for i in range(nums):
        _index = random.randint(0, _num)
        while(_index in _list):
            _index = random.randint(0,_num)
        _list.append(_index)
        re_list.append(dict[key][_index])
    if len(re_list)==1:
        return re_list[0]
    return re_list

def get_dict_list_value(dict ,father_key , key):
    '''
      这个字典的值是 list , list 里面是一堆字典 ,然后我们取list中每个字典的值
    :param dict:
    :param key:
    :return:
    '''
    _list=dict[father_key]
    re_list=[]
    for dict in _list:
        temp = map(dict ,"code" ,"无")
        if temp != "无":
            re_list.append(temp)

    return re_list

if __name__ == '__main__':
    a = {"code": 0,
         "data":
             {"organization": {"id": 22,
                               "name": "新建机构全部信息都有（勿删）",
                               "identityName": "all",
                               "logo": {"path": "/v1/20181206/iGy_0sHpe1B0H9btvRumYQ6830586a299a4868af831d2626e18274",
                                        "ossUrl": "https://static.36krcnd.com/v1/20181206/iGy_0sHpe1B0H9btvRumYQ6830586a299a4868af831d2626e18274"},
                               "hasSold": 1,
                               "briefIntro": "简介",
                               "focusDomain": "关注领域",
                               "intro": "详细介绍",
                               "capitalScale": "10000亿",
                               "closeup": "机构特写",
                               "keywords": "关键字,资本",
                               "orgUserId": 12345678,
                               "officialWebsite": "http://www.baidu.com",
                               "wechatQrcode": {
                                   "path": "/v1/20181206/YfPuR3I-qGKsl3V5g1nfMAe22b0ccad448414d8fc0133102a5274c",
                                   "ossUrl": "https://static.36krcnd.com/v1/20181206/YfPuR3I-qGKsl3V5g1nfMAe22b0ccad448414d8fc0133102a5274c"},
                               "weibo": "http://www.baidu.com"},
              "investmentList": [{"name": "项目名称", "briefIntro": "项目描述",
                                  "logo": {
                                      "path": "/v1/20181206/iGy_0sHpe1B0H9btvRumYQa7a2d31006af453a8d328a248202b165",
                                      "ossUrl": "https://static.36krcnd.com/v1/20181206/iGy_0sHpe1B0H9btvRumYQa7a2d31006af453a8d328a248202b165"},
                                  "displayOrder": 1}]}}

    print(map(a,'logo'))

    dict = {"1": [2, 3, 4, 5, 6, 7]}

    get_random_value(dict, "1", 6)

    a={'tradeList': [{'code': 4, 'msg': '互联网金融'},{'code1': 9, 'msg': '文化娱乐'},{'code': 7, 'msg': '文化娱乐'}, {'code': 9, 'msg': '文化娱乐'}]}
    get_dict_list_value(a,"tradeList" ,"code")



