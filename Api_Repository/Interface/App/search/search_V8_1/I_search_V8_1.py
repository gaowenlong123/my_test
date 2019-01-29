from Api_Server.Root_Gateway.Gateway import Gateway
from Api_Server.Support.Base_Enums import Enums
from Api_Server.Support.Base_APP import *
import os , requests ,copy ,json


class I_search_V8_1(Gateway):
    def __init__(self ,type=''):
        super(I_search_V8_1 ,self).__init__()

        self.post_data = self.get_data()
        self.request=requests.session()


    def get_dir_name(self):
        dir_name = str(os.path.dirname(__file__).split('/')[-1])
        return dir_name

    def get_url(self):
        # 在这里区分的是测试环境还是线上环境
        self.url = Enums.test_App_url_java
        return self.url

    def get_version(self):
        return version.V8_1

    def get_isLogin(self):
        return False

    def get_param(self):
        return {
            "platformId": "1",
            "siteId": "1",
        }

    def hotword(self):
        # 先处理数据
        _data = json.dumps(copy.deepcopy(self.post_data))

        # 生成签名
        sign = self.MD5(_data)
        _url = self.url + '/api/mis/nav/search/hotword?sign=' + sign

        print(sign)
        re = self.request.post(url=_url, headers=self.Headers, data=_data)
        print(re.text)

    def recom(self):
        # 先处理数据
        _data = json.dumps(copy.deepcopy(self.post_data))

        # 生成签名
        sign = self.MD5(_data)
        _url = self.url + '/api/mis/nav/search/recom?sign=' + sign

        print(sign)
        re = self.request.post(url=_url, headers=self.Headers, data=_data)
        print(re.text)

    def result(self ,word):
        # 先处理数据
        temp = copy.deepcopy(self.post_data)
        temp['param']["searchWord"] = word

        _data = json.dumps(temp)


        # 生成签名
        sign = self.MD5(_data)
        _url = self.url + '/api/mis/nav/search/result?sign=' + sign

        print(sign)
        re = self.request.post(url=_url, headers=self.Headers, data=_data)
        print(re.text)

    def result_by_type(self ,word ,type):
        # 先处理数据
        temp = copy.deepcopy(self.post_data)
        mod_data={
            "searchType": type,
            "sort": "date",
            "pageEvent": 0,
            "pageSize": 20,
            "searchWord": word,
        }
        temp["param"].update(mod_data)
        print(temp)
        _data = json.dumps(temp)

        # 生成签名
        sign = self.MD5(_data)
        _url = self.url + '/api/mis/nav/search/resultbytype?sign=' + sign

        print(sign)
        re = self.request.post(url=_url, headers=self.Headers, data=_data)
        print(re.text)



if __name__ == '__main__':

    i = I_search_V8_1()
    # i.recom()
    # i.hotword()
    # import time
    # time.sleep(1)
    # i.result("NBA")

    # i.result_by_type("资本" ,type=search_type.article)