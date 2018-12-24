from Api_Server.Support.Base_Enums import Enums
from Api_Server.Root.Interface import Interface
import os ,json , copy , requests
from Api_Server.Support.Base_Compare import map
from Api_Server.Support.Base_Time import *


class I_YellowPage(Interface):
    def __init__(self):
        super(I_YellowPage,self).__init__()

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


        self.url = 'http://mrstest43.corp.36kr.com/api'

        self.request=requests.session()

        pass

    def get_Init(self):
        '''
        :param article_id: 10465313
        :return:
        '''
        pass
        _url = self.url +"/project/addInit"
        headers = copy.deepcopy(self.Headers)
        # headers['Content-Type'] = 'application/json;charset=UTF-8'

        re= self.request.get(url=_url  ,headers=headers)
        print(re.text)

        return re.json()["data"]

    def add(self):
        pass
        _url = self.url +"/project/add"
        headers = copy.deepcopy(self.Headers)
        headers['Content-Type'] = 'application/json;charset=UTF-8'

        _data = {
            "id":1
        }

        re= self.request.get(url=_url ,headers=headers )
        print(re.text)
        # return re.json()["code"]

    def mod_Iint(self, id):
        pass
        _url = self.url + "/project/modInit/"+str(id)
        headers = copy.deepcopy(self.Headers)
        headers['Content-Type'] = 'application/json;charset=UTF-8'

        re = self.request.get(url=_url, headers=headers)
        print(re.text)

        return re.json()["data"]

    def mod(self , moddata ,data ):
        '''

        :param moddata:  修改的数据
        :param data:  模板数据
        :return: {"code":0}
        '''
        pass
        _url = self.url +"/project/mod"
        headers = copy.deepcopy(self.Headers)
        headers['Content-Type'] = 'application/json;charset=UTF-8'

        for key in moddata:
            data[key]=moddata[key]
        data.pop("entityTitle")

        re= self.request.post(url=_url ,headers=headers ,data=json.dumps(data))
        print(re.text)

    def weight_mod(self , id ,weight):
        _url = self.url + "/project/weight/mod"
        headers = copy.deepcopy(self.Headers)
        headers['Content-Type'] = 'application/json;charset=UTF-8'

        _data = {
            "id": id,
            "weight":weight
        }

        re = self.request.post(url=_url, headers=headers ,data=_data)
        print(re.text)
        # return re.json()["code"]

    def delete(self , id ):
        _url = self.url + "/project/del"
        headers = copy.deepcopy(self.Headers)
        headers['Content-Type'] = 'application/json;charset=UTF-8'

        _data = {
            "id": id
        }

        re = self.request.post(url=_url, headers=headers ,data=_data)
        print(re.text)
        # return re.json()["code"]

if __name__ == '__main__':
    i= I_YellowPage()
    # i.test_add("测试" )
    i.get_Init()
    i.add()
    a=""