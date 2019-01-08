from Api_Server.Root.Gateway import Gateway
from Api_Server.Support.Base_Enums import Enums
from Api_Server.Support.Base_APP import *
import os , requests ,copy ,json
from Api_Server.Decorate_Data.Extract_Dict_Value import *
from Api_Server.Decorate_Data.Extract_Value_Tostring import *
from Api_Server.Support.Base_Time import *


class I_channel_V8_1(Gateway):
    def __init__(self ,type=''):
        super(I_channel_V8_1 ,self).__init__()

        #===== 父类实现 生成文件，记录，登录等  ，这个类实现param的个性化接口======

        # self.param = self.get_channelType_param(type)
        self.post_data = self.get_channel_data(type)
        # print(self.post_data)
        # print(self.url)

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
        return ''

    def foces(self):
        #先处理数据
        _data = json.dumps(copy.deepcopy(self.post_data))

        #生成签名
        sign = self.MD5(_data)
        _url = self.url + '/api/mis/nav/home/subnav/recom?sign='+sign


        rep = self.request.post(url=_url , headers = self.Headers , data=_data)
        return rep.json()

    def feed(self, num):
        # 先处理数据
        temp = copy.deepcopy(self.post_data)
        temp['param']["pageEvent"] = "0"
        temp['param']["pageSize"] = str(num)

        _data = json.dumps(temp)

        headers = copy.deepcopy(self.Headers)
        headers['timestamp']= str(time_Stamp())
        # headers["Connection"]='keep-alive'
        # 生成签名
        a=requests.session()
        sign = self.MD5(_data)
        _url = self.url + '/api/mis/nav/home/subnav/flow?sign=' + sign
        print(headers)
        rep = a.post(url=_url, headers=headers, data=_data)
        return rep.json()

if __name__ == '__main__':
    i = I_channel_V8_1(channel_type.video)

    #焦点图           上下一起用会报错
    # i.foces()

    #频道信息流                      (下滑是怎么请求的  event=1)
    # data=i.feed(20)
    # data=get_dict_value(data,template_path='data/itemList')
    # # print(data)
    # keyValues_ToString(data=data, key_list=["id","widgetTitle","duration"])

    import time
    for m in range(5):
        data=i.feed(2)
        print(data)
        time.sleep(3)

