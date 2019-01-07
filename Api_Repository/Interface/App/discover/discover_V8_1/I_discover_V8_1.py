from Api_Server.Root.Gateway import Gateway
from Api_Server.Support.Base_Enums import Enums
from Api_Server.Support.Base_APP import *
import os , requests ,copy ,json


class I_discover_V8_1(Gateway):
    def __init__(self ,type=''):
        super(I_discover_V8_1 ,self).__init__()

        self.post_data = self.get_data()
        self.request=requests.session()


    def get_dir_name(self):
        dir_name = str(os.path.dirname(__file__).split('/')[-1])
        return dir_name

    def get_url(self):
        # 在这里区分的是测试环境还是线上环境
        self.url = Enums.test_App_url
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

    def foces(self):
        # 先处理数据
        _data = json.dumps(copy.deepcopy(self.post_data))

        # 生成签名
        sign = self.MD5(_data)
        _url = self.url + '/api/mis/nav/discover/recom?sign=' + sign

        rep = self.request.post(url=_url, headers=self.Headers, data=_data)

        return rep.json()

    def feed(self, num=20):
        # 先处理数据
        temp = copy.deepcopy(self.post_data)
        temp['param']["pageEvent"] = "0"
        temp['param']["pageSize"] = str(num)

        _data = json.dumps(temp)

        # 生成签名
        sign = self.MD5(_data)
        _url = self.url + '/api/mis/nav/discover/flow?sign=' + sign

        rep = self.request.post(url=_url, headers=self.Headers, data=_data)
        print(rep.text)
        return rep.json()


if __name__ == '__main__':
    i = I_discover_V8_1()
    # i.foces()
    # i.feed()