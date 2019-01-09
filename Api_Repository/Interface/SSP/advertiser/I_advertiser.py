from Api_Server.Support.Base_Enums import Enums
from Api_Server.Root.Interface import Interface
import os ,json , copy , requests
from Api_Server.Support.Base_Compare import map


class I_advertiser(Interface):
    def __init__(self):
        super(I_advertiser,self).__init__()




    def get_dir_name(self):
        #外部调用的路径
        path=str(os.path.dirname(__file__).split('/')[-1])+'\\'+str(os.path.dirname(__file__).split('/')[-1].split("\\")[-1])

        return str(os.path.dirname(__file__).split('/')[-1])

    def get_url(self):
        return Enums.test_Mrs_url

    def get_post_Data(self , para):
        return {}

    def _public_property(self):
        self.url = 'http://ssptest28.36kr.com/api/crm/advertiser'

        self.request = requests.session()

        self.templet_data = {}

        self.mod_data = {}

    def get_list(self):
        _url = self.url + "/list?param.pageNo=1&param.pageSize=10"
        headers = copy.deepcopy(self.Headers)

        rep = self.request.get(url=_url, headers=headers)

        return rep.json()["code"]

    def add(self ,name):  # 表单提交
        pass
        _url = self.url + "/add"
        headers = copy.deepcopy(self.Headers)
        headers['Content-Type'] = 'application/x-www-form-urlencoded'

        _data = {
                    "param.name": name,
                    # "param.remark":
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
            return []

    def mod(self ,data , isStatus=True ):  # 表单提交
        pass
        _url = self.url + "/mod"
        headers = copy.deepcopy(self.Headers)
        headers['Content-Type'] = 'application/x-www-form-urlencoded'

        _data = {
                    "param.name": data["name"],
                    "param.status" : 1 if isStatus else 0 ,
                     # "param.remark":
                    "param.id":data["id"],
        }
        if data.get('remark' ,None) != None:
            _data.update({'remark': data["remark"]})
        print(_data)

        rep = self.request.post(url=_url, headers=headers, data=_data)
        # print(rep.json())
        return rep.json()

if __name__ == '__main__':
    i = I_advertiser()
    # i.add("测试123")
    # i.get_list()


    # data=i.get_detail(45)
    # i.mod(data , isStatus=False)