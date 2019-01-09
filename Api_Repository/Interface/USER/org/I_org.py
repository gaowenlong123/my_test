from Api_Server.Support.Base_Enums import Enums
from Api_Server.Root.Interface import Interface
import os ,json , copy , requests
from Api_Server.Support.Base_Compare import map


class I_org(Interface):
    def __init__(self):
        super(I_org,self).__init__()


    def get_dir_name(self):
        #外部调用的路径
        path=str(os.path.dirname(__file__).split('/')[-1])+'\\'+str(os.path.dirname(__file__).split('/')[-1].split("\\")[-1])

        return str(os.path.dirname(__file__).split('/')[-1])

    def get_url(self):
        return Enums.test_Mrs_url

    def get_post_Data(self , para):
        return {}

    def _public_property(self):
        self.url = 'http://ssotest27.36kr.com/api/sys/org'

        self.request = requests.session()

        self.templet_data = {}

        self.mod_data = {}

    def get_list(self,num=20):
        _url = self.url + "/list"
        headers = copy.deepcopy(self.Headers)

        data={
            "param" :{
                "pageNo" : 1,
                 "pageSize" :num,
            }
        }

        rep = self.request.post(url=_url, headers=headers,data=json.dumps(data))
        # print(rep.json())
        return rep.json()["code"]


    def add(self ,name ,parentId):
        pass
        _url = self.url + "/add"
        headers = copy.deepcopy(self.Headers)

        _data = {
                "param" :{
                     "name" : name,
                     "parentId" :parentId,
            }
        }

        rep = self.request.post(url=_url, headers=headers, data=json.dumps(_data))
        print(rep.json())
        return rep.json()

    def get_detail(self ,id):
        _url = self.url + "/modInit"
        re_dict = {}
        _data = {
            "param": {

                "id": id,
            }
        }
        rep = self.request.post(url=_url, headers=self.Headers ,data=json.dumps(_data))
        print(rep.json())
        try:
            temp= rep.json()["data"]
            re_dict ={
                "id":temp["id"],
                "name":temp["id"],
                "parentId":temp["id"]
            }
            if temp.get("remark" ,None) !=None:
                re_dict.update({"remark" ,temp["remark"]})
            return re_dict
        except:
            return re_dict

    def mod(self ,data , mod_data ):  # 如果创建时没有 remaek  就不修改 remark
        '''
        :param data:
        :param mod_data:    name  parentId   remark
        :return:
        '''
        _url = self.url + "/mod"
        headers = copy.deepcopy(self.Headers)

        for key in mod_data:
            if data.get(key , None) !=None:
                data[key] = mod_data[key]

        rep = self.request.post(url=_url, headers=headers, data=json.dumps(data))
        print(rep.json())
        return rep.json()

if __name__ == '__main__':
    i = I_org()
    i.get_list()

    #没有验证