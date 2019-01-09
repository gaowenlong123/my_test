from Api_Server.Support.Base_Enums import Enums
from Api_Server.Root.Interface import Interface
import os ,json , copy , requests
from Api_Server.Support.Base_Compare import map


class I_panel(Interface):
    def __init__(self):
        super(I_panel,self).__init__()




    def get_dir_name(self):
        #外部调用的路径
        path=str(os.path.dirname(__file__).split('/')[-1])+'\\'+str(os.path.dirname(__file__).split('/')[-1].split("\\")[-1])

        return str(os.path.dirname(__file__).split('/')[-1])

    def get_url(self):
        return Enums.test_Mrs_url

    def get_post_Data(self , para):
        return {}

    def _public_property(self):
        self.url = 'http://ssptest28.36kr.com/api/flow/panel'

        self.request = requests.session()

        self.templet_data = {}

        self.mod_data = {}

    def get_list(self):
        _url = self.url + "/list?param.pageNo=1&param.pageSize=10"
        headers = copy.deepcopy(self.Headers)

        rep = self.request.get(url=_url, headers=headers)

        return rep.json()["code"]

    def add(self ,width ,height):  # 表单提交
        pass
        _url = self.url + "/add"
        headers = copy.deepcopy(self.Headers)
        headers['Content-Type'] = 'application/x-www-form-urlencoded'

        _data = {
                    "param.width": width,
                    "param.height": height,
        }

        rep = self.request.post(url=_url, headers=headers, data=_data)
        # print(rep.json())
        return rep.json()

    def get_detail(self ,id):
        _url = self.url + "/detail?param.id="+str(id)
        rep = self.request.get(url=_url, headers=self.Headers)
        try:
            return rep.json()["data"]["advertiser"]
        except:
            print("请重新取值")
            return []

    def mod(self ,data ,mod_data):  # 表单提交
        '''

        :param data:
        :param mod_data:    param.width"     param.height":
        }
        :return:
        '''
        _url = self.url + "/mod"
        headers = copy.deepcopy(self.Headers)
        headers['Content-Type'] = 'application/x-www-form-urlencoded'

        for key in mod_data:
            data[key] = mod_data[key]


        rep = self.request.post(url=_url, headers=headers, data=data)
        # print(rep.json())
        return rep.json()

if __name__ == '__main__':
    pass
    #没有验证