
# 获取字典中的objkey对应的值，适用于字典嵌套
# dict:字典
# objkey:目标key
# default:找不到时返回的默认值
def map(dict, objkey, default):
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

    print(map(a,'logo','444'))