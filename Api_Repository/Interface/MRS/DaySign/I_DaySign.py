from Api_Server.Support.Base_Enums import Enums
from Api_Server.Root.Interface import Interface
import os ,json , copy , requests
from Api_Server.Support.Base_Compare import map
from Api_Server.Support.Base_Time import *


class I_DaySign(Interface):
    def __init__(self):
        super(I_DaySign,self).__init__()

        pass




    def get_dir_name(self):
        #外部调用的路径
        path=str(os.path.dirname(__file__).split('/')[-1])+'\\'+str(os.path.dirname(__file__).split('/')[-1].split("\\")[-1])

        return str(os.path.dirname(__file__).split('/')[-1])

    def get_url(self):
        return Enums.test_Mrs_url

    def get_post_Data(self , para):
        return {}

    def _public_property(self):
        # 显示标题 ，外链
        self.post_data = {
                           "effectTime":"",
                            "entityId": 0,
                            "content": "内容",
                             "title": ""}


        self.url = 'http://mis-test.corp.36kr.com/api'

        self.request=requests.session()


    def test_add(self , title, article_id =10465313 , day=0):
        '''
        :param article_id: 10465313
        :return:
        '''
        pass
        _url = self.url +"/mis/dailyword/add"
        headers = copy.deepcopy(self.Headers)
        headers['Content-Type'] = 'application/json;charset=UTF-8'

        _data = {
            "effectTime":get_late_baseday(day),
            "entityId": article_id,
            "content": "内容",
            "title": title

        }

        re= self.request.post(url=_url ,headers=headers ,data=json.dumps(_data))
        print(re.text)

    def test_ID(self ,id ):

        pass
        _url = self.url +"/mis/dailyword/entity"
        headers = copy.deepcopy(self.Headers)
        headers['Content-Type'] = 'application/x-www-form-urlencoded'

        _data = {
            "id":id
        }

        re= self.request.post(url=_url ,headers=headers ,data=json.dumps(_data))
        print(re.text)
        return re.json()["code"]


    def mod_day(self ,moddata):
        data=self.test_modIint(moddata)
        self.test_mod(moddata=moddata,data=data)

    def test_modIint(self, moddata):
        pass
        _url = self.url + "/mis/dailyword/modInit"
        headers = copy.deepcopy(self.Headers)
        headers['Content-Type'] = 'application/json;charset=UTF-8'

        _data = {
            "id": moddata["id"]
        }

        re = self.request.post(url=_url, headers=headers, data=json.dumps(_data))
        print(re.text)

        return re.json()["data"]

    def test_mod(self , moddata ,data ):
        '''

        :param moddata:  修改的数据
        :param data:  模板数据
        :return: {"code":0}
        '''
        pass
        _url = self.url +"/mis/dailyword/mod"
        headers = copy.deepcopy(self.Headers)
        headers['Content-Type'] = 'application/json;charset=UTF-8'

        for key in moddata:
            data[key]=moddata[key]
        data.pop("entityTitle")

        re= self.request.post(url=_url ,headers=headers ,data=json.dumps(data))
        print(re.text)




if __name__ == '__main__':
    i= I_DaySign()
    # i.test_add("测试" )
    i.test_ID(10465313)  # {"code":99,"msg":"没有权限，请重新登录"}    是因为X-token的原因吗？？？
