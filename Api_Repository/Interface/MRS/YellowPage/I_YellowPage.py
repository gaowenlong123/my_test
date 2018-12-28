from Api_Server.Support.Base_Enums import Enums
from Api_Server.Root.Interface import Interface
import os ,json , copy , requests
from Api_Server.Support.Base_Compare import *
from Api_Server.Support.Base_Time import *
from Api_Repository.Data_Center.yellowPage import *
from Api_Server.Support.Base_Data import *

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
        self.post_data = {"param":
            {"name":"",
              "logoUrl":logurl.logo,
              "status":0,
              "trade":"",
              "round":0,
              "address":"110000,110000,110105",
              "scale":0,
              "establishTime":"2018-01-01",
              "identityName":"",
              "briefIntro":"一句话简介",
              "intro":"项目介绍",
              "space":"<p><strong><span style=\"color:#07a9fe\">市场空间与格局</span></strong></p>",
              "corePower":"<p><span style=\"color:#f32784\"><strong><em>核心竞争力</em></strong></span></p>",
              "articleId":"",
              "businessModel":"<p><span style=\"font-size:40px\"><em>商业模式</em></span></p>",
              "officialWebsite":"http://www.baidu.com",
              "wechatQrcode":wechatQrcode.phone,
              "weibo":"http://www.baidu.com",
              "teamMemberList":teamMemberList.team}}


        self.url = 'http://mrstest43.corp.36kr.com/api'

        self.request=requests.session()

        pass

    def get_Init(self ,is_open=True):
        '''
        :param article_id: 10465313
        :return:
        '''
        pass
        _url = self.url +"/project/addInit"
        headers = copy.deepcopy(self.Headers)
        _temp = {}
        re_dict={}
        # headers['Content-Type'] = 'application/json;charset=UTF-8'
        re= self.request.get(url=_url  ,headers=headers)

        try:
            _temp = re.json()["data"]
            re_dict["tradeList"]=get_random_value(_temp ,"tradeList" ,2)
            re_dict["roundList"]=get_random_value(_temp ,"roundList" ,1)
            re_dict["scaleList"] = get_random_value(_temp, "scaleList", 1)
            if is_open:
                re_dict["statusList"] = _temp["statusList"][0]["code"]
            else:
                re_dict["statusList"] = _temp["statusList"][1]["code"]

            re_dict["tradeList"] = get_dict_list_value(re_dict ,"tradeList" ,"code")

        except:
            print("critil error")

        return re_dict              #值是一个字典


    def add(self , name ,mod_data ,article_Id=None ):
        _url = self.url + "/project/add"
        headers = copy.deepcopy(self.Headers)
        _data = copy.deepcopy(self.post_data)
        headers['Content-Type'] = 'application/json;charset=UTF-8'

        _data["param"]["name"]=name
        _data["param"]["identityName"]="project"+str(time_Stamp())
        _data["param"]["status"] = mod_data["statusList"]
        _data["param"]["trade"] = list_ToString(mod_data["tradeList"])
        _data["param"]["round"] = mod_data["roundList"]["code"]
        _data["param"]["scale"] = mod_data["scaleList"]["code"]
        if article_Id ==None:
            _data["param"]["articleId"] = "10465604,10465634"
        else:
            _data["param"]["articleId"] = list_ToString(article_Id)
        # print(_data["param"]["identityName"])

        re= self.request.post(url=_url ,headers=headers ,data=json.dumps(_data))
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
            修改暂时不写了吧
        :param moddata:  修改的数据
        :param data:  模板数据
        :return: {"code":0}
        '''
        pass


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
        headers['Content-Type'] = 'application/x-www-form-urlencoded'

        _data = {
            "param.id": id
        }
        re = self.request.post(url=_url, headers=headers ,data=_data)
        print(re.text)
        # return re.json()["code"]

if __name__ == '__main__':
    i= I_YellowPage()
    # i.test_add("测试" )

    # for m in range(1):
    #     data=i.get_Init()
    #     i.add("测试黄页"+str(m) ,mod_data=data ,article_Id=[])  #文章只能关联一个项目
    #     time.sleep(2)

    i.delete(150)