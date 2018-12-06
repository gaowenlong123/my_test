from Base.Support.Base_Enums import Enums
from Base.Root.Interface import Interface
from Picture.Picture import Picture
import os ,json
import requests


class I_vClub(Interface):
    def __init__(self):
        super(I_vClub,self).__init__()

        self.url='http://mrstest43.corp.36kr.com/api/organ/organization/'

        self.request=requests.session()

        self.must_str=["name" ,"logoUrl","hasSold" ,"identityName" , "briefIntro" , "focusDomain" , "intro" ,"investmentCaseList" ]

        #修改数据 缺少ID
        self.templet_unSold_data={"param":
        {"name":"",
         "logoUrl":"",
         "hasSold":"0"}}

        self.templet_data={"param":
        {"name":"机构名必填",
        "hasSold":"1",
        "identityName":"shige",
        "briefIntro":"简介",
        "focusDomain":"关注领域",
        "intro":"详细介绍",
        "capitalScale":"资金规模",
        "closeup":"机构特写",
        "keywords":"关键字,资本",
        "orgUserId":"1234567",
        "officialWebsite":"http://",
        "wechatQrcode":"",
        "weibo":"http://",
        "investmentCaseList":[{"name":"0","briefIntro":"0","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA94fa28b4b5f845b4bf6783e110258d28","displayOrder":1},{"name":"1","briefIntro":"1","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA666b34334e214dbe991e91001e4757be","displayOrder":2},{"name":"2","briefIntro":"2","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA79c7ae6f33f6419791601f401fa5a1f9","displayOrder":3},{"name":"3","briefIntro":"3","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA3823d8cbf6d1450cbf097b83ad6f5dd5","displayOrder":4},{"name":"4","briefIntro":"4","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA6cc30c98b6ec4bcb9d796e16e1e48c08","displayOrder":5},{"name":"5","briefIntro":"5","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA62c0b981c5d34060a01d4bd600e83d37","displayOrder":6},{"name":"6","briefIntro":"6","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA52e47b7144494b74a830d12e4592a1c8","displayOrder":7},{"name":"7","briefIntro":"7","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA4a8a079b912848a1a00f60e9bbd936b5","displayOrder":8},{"name":"8","briefIntro":"8","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA73670c3a07ce4259800cbacb1c4aec47","displayOrder":9},{"name":"9","briefIntro":"9","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA11e2f7d8a0574cccb4ab1e8f618ded0a","displayOrder":10}],
        "logoUrl":"/v1/20181206/iGy_0sHpe1B0H9btvRumYQ6a2fedb92f5843258e8e179f2bd6257c",}}


    def get_dir_name(self):
        return str(os.path.dirname(__file__).split('/')[-1])

    def get_url(self):
        return Enums.test_Mrs_url

    def get_post_Data(self , para):
        return {}


    #接口方法
    def get_feed(self ,pageSize=10 ,pageNo=1):
        '''
        :url: list?param.pageSize=10&param.pageNo=1
        :type: get
        :return:  json
        '''
        _url='list?param.pageSize='+str(pageSize)+'&param.pageNo='+str(pageNo)
        request_url = self.url+_url
        re=self.request.get(url=request_url ,headers=self.Headers)
        print('获得信息流  ==>> ',re.text)

    def get_mod_init(self ,id):
        '''
        :url  :  modinit?param.id=81
        :return: json
        '''
        _url =  'modinit?param.id='+str(id)
        request_url = self.url+_url

        re=self.request.get(url=request_url , headers=self.Headers)
        print(re.text)

    #新建是没有id ，post到服务器后才生产 id
    def add(self ,data ,is_sold=False):
        '''
        :url:  add
        :type:  post
        :data:           不限制错误数据

        :return: {"code":0}
        '''
        #基本数据
        _url='add'
        request_url = self.url + _url

       #业务逻辑部分
        if is_sold:
            for key in data:
                print(key)
            # self.templet_data['param']['logoUrl']



            re=self.request.post(url=request_url ,data=json.dumps(self.templet_data) ,headers=self.Headers)
        else:
            self.templet_unSold_data['param']['logoUrl']=data['logoUrl']
            self.templet_unSold_data['param']['name']=data['name']
            #请求
            re=self.request.post(url=request_url ,data=json.dumps(self.templet_unSold_data) ,headers=self.Headers)

        print(re.text)

    #直接post传入的参数
    def add_param(self,data):
        '''
        '''
        # 基本数据
        _url = 'add'
        request_url = self.url + _url

        #全部都有的参数，当做模板格式
        post_data = {}


        # 请求
        re = self.request.post(url=request_url, data=json.dumps(data), headers=self.Headers)
        print(re.text)

#没有写
    def mod(self , name='' ,is_sold=False):
        '''
        :url:  add
        :type:  post
        :mod_data:  {"param":
        {"name":"该机构有十个投资案例（勿删）",
        "hasSold":"1",
        "identityName":"shige",
        "briefIntro":"简介",
        "focusDomain":"关注领域",
        "intro":"详细介绍",
        "capitalScale":"11111111111111111111",
        "closeup":"1111111",
        "keywords":"文章关键字,资本",
        "orgUserId":"12345678",
        "officialWebsite":"http://",
        "wechatQrcode":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMAd18887066ffc480d89c7e8892de7668f",
        "weibo":"http://",
        "investmentCaseList":[{"name":"0","briefIntro":"0","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA94fa28b4b5f845b4bf6783e110258d28","displayOrder":1},{"name":"1","briefIntro":"1","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA666b34334e214dbe991e91001e4757be","displayOrder":2},{"name":"2","briefIntro":"2","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA79c7ae6f33f6419791601f401fa5a1f9","displayOrder":3},{"name":"3","briefIntro":"3","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA3823d8cbf6d1450cbf097b83ad6f5dd5","displayOrder":4},{"name":"4","briefIntro":"4","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA6cc30c98b6ec4bcb9d796e16e1e48c08","displayOrder":5},{"name":"5","briefIntro":"5","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA62c0b981c5d34060a01d4bd600e83d37","displayOrder":6},{"name":"6","briefIntro":"6","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA52e47b7144494b74a830d12e4592a1c8","displayOrder":7},{"name":"7","briefIntro":"7","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA4a8a079b912848a1a00f60e9bbd936b5","displayOrder":8},{"name":"8","briefIntro":"8","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA73670c3a07ce4259800cbacb1c4aec47","displayOrder":9},{"name":"9","briefIntro":"9","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA11e2f7d8a0574cccb4ab1e8f618ded0a","displayOrder":10}],
        "logoUrl":"/v1/20181206/iGy_0sHpe1B0H9btvRumYQ33a0c3f2a0f0445d82df9433d3ece568",
        "id":"10"}}

        :return: {"code":0}




        '''


        pass

    def mod_param(self ,data , id ):
        '''
        :url : mod
        :param data:  参数要带上ID
        :return:
        '''
        header=self.Headers
        header['Content-Type']='application/json;charset=UTF-8'
        _url= 'mod'
        request_url = self.url + _url

        if data['param'].get('id', None) == None:
            data['param'].update({'id':id})
        print(data)
        # 请求
        re = self.request.post(url=request_url, data=json.dumps(data), headers=header)
        print(re.text)


    def modWeight(self ,id , weight):
        '''
        :param weight: 权重
        :return:
        '''
        headers = self.Headers
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        _url='modWeight'
        request_url = self.url + _url

        post_data={'param.id':id,'param.weight':weight}


        re=self.request.post(url=request_url ,data=post_data ,headers=headers)
        print(re)

    def delete(self,id):
        '''
        url:  del
        :type: post
        :post_data:  param.id=4
        :return: {"code":0}
        '''
        headers=self.Headers
        headers['Content-Type']= 'application/x-www-form-urlencoded'
        _url='del'
        post_data = {'param.id':str(id)}
        request_url = self.url+_url


        re=self.request.post(url=request_url ,data=post_data ,headers=headers)
        print(re.text)





if __name__ == '__main__':
    i =I_vClub()
    # i.get_feed()
    # i.delete(15)
    # i.modWeight(2,100)
    # i.get_mod_init(20)
    # i.mod_param(data, 18)

    # i.add(data={'name':'z自动化','logoUrl':Picture.car},is_sold=False)



    data={"name":"该机构有十个投资案例（误删）",
        "hasSold":"1",
        "identityName":"shige",
        "briefIntro":"简介",
        "focusDomain":"关注领域",
        "intro":"详细介绍",
        "capitalScale":"资金规模",
        "closeup":"机构特写",
        "keywords":"关键字,资本",
        "orgUserId":"1234567",
        "officialWebsite":"http://",
        "wechatQrcode":"",
        "weibo":"http://",
        "investmentCaseList":[{"name":"0","briefIntro":"0","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA94fa28b4b5f845b4bf6783e110258d28","displayOrder":1},{"name":"1","briefIntro":"1","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA666b34334e214dbe991e91001e4757be","displayOrder":2},{"name":"2","briefIntro":"2","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA79c7ae6f33f6419791601f401fa5a1f9","displayOrder":3},{"name":"3","briefIntro":"3","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA3823d8cbf6d1450cbf097b83ad6f5dd5","displayOrder":4},{"name":"4","briefIntro":"4","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA6cc30c98b6ec4bcb9d796e16e1e48c08","displayOrder":5},{"name":"5","briefIntro":"5","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA62c0b981c5d34060a01d4bd600e83d37","displayOrder":6},{"name":"6","briefIntro":"6","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA52e47b7144494b74a830d12e4592a1c8","displayOrder":7},{"name":"7","briefIntro":"7","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA4a8a079b912848a1a00f60e9bbd936b5","displayOrder":8},{"name":"8","briefIntro":"8","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA73670c3a07ce4259800cbacb1c4aec47","displayOrder":9},{"name":"9","briefIntro":"9","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA11e2f7d8a0574cccb4ab1e8f618ded0a","displayOrder":10}],
        "logoUrl":"/v1/20181206/iGy_0sHpe1B0H9btvRumYQ6a2fedb92f5843258e8e179f2bd6257c",}

    i.add(data,is_sold=True)



    #自由风格的  新建和添加


    # for m in range(50):
        # data['param']['name']=m
        # data['param']['identityName'] = m
        # i.add_param(data=data,is_diret=True  )
        # import time
        # time.sleep(1)
        # m+=50
        # i.add(name=str(m))