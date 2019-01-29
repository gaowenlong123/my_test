from Api_Server.Root_Gateway.Gateway import Gateway
from Api_Server.Support.Base_Enums import Enums
from Api_Server.Support.Base_APP import *
import os , requests ,copy ,json


class I_copartner_V8_1(Gateway):
    def __init__(self ,type=''):
        super(I_copartner_V8_1 ,self).__init__()

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

    def feed(self):
        # 先处理数据
        temp = copy.deepcopy(self.post_data)
        mod_data = {
            "pageSize": 20,
            "pageEvent": 0
        }
        temp["param"].update(mod_data)
        _data = json.dumps(temp)

        # 生成签名
        sign = self.MD5(_data)
        _url = self.url + '/api/mis/nav/copartner/flow?sign=' + sign

        print(sign)
        re = self.request.post(url=_url, headers=self.Headers, data=_data)
        print(re.text)



    def detail(self , id ):
        # 先处理数据
        temp = copy.deepcopy(self.post_data)
        mod_data = {
            "feedId": id,
        }
        temp["param"].update(mod_data)
        _data = json.dumps(temp)

        # 生成签名
        sign = self.MD5(_data)
        _url = self.url + '/api/mis/nav/copartner/detail?sign=' + sign

        print(sign)
        re = self.request.post(url=_url, headers=self.Headers, data=_data)
        print(re.text)



if __name__ == '__main__':
    i = I_copartner_V8_1()
    # i.feed()
    i.detail(id=196)
