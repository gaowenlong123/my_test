from Api_Server.Support.Base_Enums import Enums
from Api_Server.Root.Interface import Interface
import os ,json , copy , requests
from Api_Server.Support.Base_Compare import map


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
        {"name":"",
        "hasSold":"",
        "identityName":"",
        "briefIntro":"",
        "focusDomain":"",
        "intro":"",
        "capitalScale":"",
        "closeup":"",
        "keywords":"",
        "orgUserId":"",
        "officialWebsite":"http://",
        "wechatQrcode":"",
        "weibo":"http://",
        "investmentCaseList":[],
        "logoUrl":"",}}

        self.mod_data={"param":
                           {"name":"test54.172222333",
                            "hasSold":"1",
                            "identityName":"ccc",
                            "briefIntro":"简介",
                            "focusDomain":"关注领域",
                            "intro":"详细介绍",
                            "capitalScale":"资金规模",
                            "closeup":"12344",
                            "keywords":"关键字,资本",
                            "orgUserId":1234567,
                            "officialWebsite":"http://1111",
                            "wechatQrcode":"",
                            "weibo":"http://",
                            "investmentCaseList":[{"name":"0","briefIntro":"0","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA94fa28b4b5f845b4bf6783e110258d28","displayOrder":1},{"name":"1","briefIntro":"1","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA666b34334e214dbe991e91001e4757be","displayOrder":2},{"name":"2","briefIntro":"2","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA79c7ae6f33f6419791601f401fa5a1f9","displayOrder":3},{"name":"3","briefIntro":"3","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA3823d8cbf6d1450cbf097b83ad6f5dd5","displayOrder":4},{"name":"4","briefIntro":"4","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA6cc30c98b6ec4bcb9d796e16e1e48c08","displayOrder":5},{"name":"5","briefIntro":"5","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA62c0b981c5d34060a01d4bd600e83d37","displayOrder":6},{"name":"6","briefIntro":"6","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA52e47b7144494b74a830d12e4592a1c8","displayOrder":7},{"name":"7","briefIntro":"7","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA4a8a079b912848a1a00f60e9bbd936b5","displayOrder":8},{"name":"8","briefIntro":"8","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA73670c3a07ce4259800cbacb1c4aec47","displayOrder":9},{"name":"9","briefIntro":"9","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA11e2f7d8a0574cccb4ab1e8f618ded0a","displayOrder":10}],
                            "logoUrl":"/v1/20181206/iGy_0sHpe1B0H9btvRumYQ6a2fedb92f5843258e8e179f2bd6257c",
                            "id":"163"}}


    def get_dir_name(self):
        #外部调用的路径
        path=str(os.path.dirname(__file__).split('/')[-1])+'\\'+str(os.path.dirname(__file__).split('/')[-1].split("\\")[-1])

        return str(os.path.dirname(__file__).split('/')[-1])

    def get_url(self):
        return Enums.test_Mrs_url

    def get_post_Data(self , para):
        return {}

    def _public_property(self):
        pass

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
       :return: json
        '''
        #售出
        a = {"code": 0,
             "data":
                 {"organization":{"id": 22,
                                    "name": "新建机构全部信息都有（勿删）",
                                     "identityName": "all",
                                        "logo": {"path": "/v1/20181206/iGy_0sHpe1B0H9btvRumYQ6830586a299a4868af831d2626e18274",
                                                 "ossUrl": "https://static.36krcnd.com/v1/20181206/iGy_0sHpe1B0H9btvRumYQ6830586a299a4868af831d2626e18274"},
                       "hasSold": 1,
                       "briefIntro": "简介",
                       "focusDomain": "关注领域",
                       "intro": "详细介绍",
                       "capitalScale": "10000亿",
                       "closeup": "机构特写",
                       "keywords": "关键字,资本",
                       "orgUserId": 12345678,
                       "officialWebsite": "http://www.baidu.com",
                       "wechatQrcode": {"path": "/v1/20181206/YfPuR3I-qGKsl3V5g1nfMAe22b0ccad448414d8fc0133102a5274c",
                                        "ossUrl": "https://static.36krcnd.com/v1/20181206/YfPuR3I-qGKsl3V5g1nfMAe22b0ccad448414d8fc0133102a5274c"},
                       "weibo": "http://www.baidu.com"},
                  "investmentList": [{"name": "项目名称", "briefIntro": "项目描述",
                                      "logo": {
                                          "path": "/v1/20181206/iGy_0sHpe1B0H9btvRumYQa7a2d31006af453a8d328a248202b165",
                                          "ossUrl": "https://static.36krcnd.com/v1/20181206/iGy_0sHpe1B0H9btvRumYQa7a2d31006af453a8d328a248202b165"},
                                      "displayOrder": 1}]}}
        #未售出  ,如果是为售出的转换到售出，是有参数的
        b={'code': 0,
           'data': {'organization':
                        {'id': 19,
                         'name': '图片是山1',
                         'logo': {'path': '/v1/20181206/iGy_0sHpe1B0H9btvRumYQf4b07b06a6c34d74928b1eae81debe4b',
                                  'ossUrl': 'https://static.36krcnd.com/v1/20181206/iGy_0sHpe1B0H9btvRumYQf4b07b06a6c34d74928b1eae81debe4b'},
                         'hasSold': 0},
                    'investmentList': []}}

        _url =  'modinit?param.id='+str(id)
        request_url = self.url+_url

        re=self.request.get(url=request_url , headers=self.Headers)
        print(re.json())
        return re.json()  #返回时 dict

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
        temp=copy.deepcopy(self.templet_data)

       #业务逻辑部分
        if is_sold:
            for key in data:
                print(key)
                temp['param'][key]=data[key]

            re=self.request.post(url=request_url ,data=json.dumps(temp) ,headers=self.Headers)
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

        # 请求
        re = self.request.post(url=request_url, data=json.dumps(data), headers=self.Headers)
        print(re.text)


    def mod(self , data ,id ,is_sold=False):
        '''
        :url:  add
        :type:  post
        :mod_data:
        :return: {"code":0}
        '''
        headers = copy.deepcopy(self.Headers)
        temp = copy.deepcopy(self.templet_data)
        unSold_temp = copy.deepcopy(self.templet_unSold_data)

        headers['Content-Type'] = 'application/json;charset=UTF-8'
        _url = 'mod'
        request_url = self.url + _url

        raw = self.get_mod_init(id)
        print('raw',raw)

        #1先将存在的数据 ，写入模板中
        for key in temp['param']:
            a = map(raw ,key ,None)
            print(key , a)
            if a != None:
                if key == 'wechatQrcode':
                    temp['param'][key]=a['path']

                temp['param'][key] = a
            else:
                if key == 'logoUrl':  # ?????
                    temp['param'][key] = raw['data']['organization']['logo']['path']
                if key=='investmentCaseList':
                    # print(raw['data']['investmentList'])
                    temp['param'][key] = raw['data']['investmentList']

        # 添加ID
        if map(raw,'id', None)!= None:
            temp['param'].update({'id': id})
        print('请求回来的值====>>>', temp)

        for key in data:  #不需要 ID 和是否售出
            print('要修改的值====>>>',key)
            temp['param'][key] = data[key]
        print('修改的值=====>>>', temp)

        if is_sold:
            temp['param']['hasSold']=1
            re=self.request.post(url=request_url ,data=json.dumps(temp) ,headers=self.Headers)
        else:
            for key in ('name','logoUrl'):
                unSold_temp['param'][key] = temp['param'][key]
            unSold_temp['param']['hasSold']=0
            unSold_temp['param'].update({'id':id})
            print('售出改为非售出的值',unSold_temp)
            # 请求
            re = self.request.post(url=request_url, data=json.dumps(unSold_temp), headers=self.Headers)

        print(re.text)

    #直接修改
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

        # 请求
        re = self.request.post(url=request_url, data=json.dumps(data), headers=header)
        print(re.text)


    def modWeight(self ,id , weight):
        '''
        :param weight: 权重
        :return:
        '''
        headers = copy.deepcopy(self.Headers)
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
        headers = copy.deepcopy(self.Headers)
        headers['Content-Type']= 'application/x-www-form-urlencoded'
        _url='del'
        post_data = {'param.id':str(id)}
        request_url = self.url+_url

        re=self.request.post(url=request_url ,data=post_data ,headers=headers)
        print(re.text)

    def Element(self):
        '''  请求页面的接口值'''
        raw=self.get_mod_init(id=1)
        print(raw['data']['organization']['hasSold'])
        print(raw['data']['organization']['id'])
        print(raw['data']['organization']['name'])
        print(raw['data']['organization']['identityName'])
        print(raw['data']['organization']['logo']['path'])
        print(raw['data']['organization']['briefIntro'])
        print(raw['data']['organization']['focusDomain'])
        print(raw['data']['organization']['intro'])
        print(raw['data']['organization']['capitalScale'])
        print(raw['data']['organization']['orgUserId'])
        print(raw['data']['organization']['officialWebsite'])
        print(raw['data']['organization']['wechatQrcode']['path'])
        print(raw['data']['organization']['weibo'])
        print(raw['data']['investmentList'])

        #



if __name__ == '__main__':
    i =I_vClub()
    i.get_feed()
    # i.delete(1)
    # i.modWeight(2,100)
    # raw=i.get_mod_init(44)
    # i.mod_param(data, 19)

    # i.add(data={'name':'z自动化','logoUrl':Picture.car},is_sold=False)
    # i.add(data,is_sold=True)

    # i.mod({'name':'nihao1','keywords':'aaaaaaa','focusDomain':'NBA'},id=44,is_sold=True)

    data={"name":"测试Vclub",
        "hasSold":"1",
        "identityName":"vclub",
        "briefIntro":"简介",
        "focusDomain":"关注领域",
        "intro":"详细介绍",
        "capitalScale":"资金规模",
        "closeup":"12344",
        "keywords":"关键字,资本",
        "orgUserId":"1234567",
        "officialWebsite":"http://",
        "wechatQrcode":"",
        "weibo":"http://",
        "investmentCaseList":[{"name":"0","briefIntro":"0","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA94fa28b4b5f845b4bf6783e110258d28","displayOrder":1},{"name":"1","briefIntro":"1","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA666b34334e214dbe991e91001e4757be","displayOrder":2},{"name":"2","briefIntro":"2","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA79c7ae6f33f6419791601f401fa5a1f9","displayOrder":3},{"name":"3","briefIntro":"3","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA3823d8cbf6d1450cbf097b83ad6f5dd5","displayOrder":4},{"name":"4","briefIntro":"4","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA6cc30c98b6ec4bcb9d796e16e1e48c08","displayOrder":5},{"name":"5","briefIntro":"5","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA62c0b981c5d34060a01d4bd600e83d37","displayOrder":6},{"name":"6","briefIntro":"6","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA52e47b7144494b74a830d12e4592a1c8","displayOrder":7},{"name":"7","briefIntro":"7","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA4a8a079b912848a1a00f60e9bbd936b5","displayOrder":8},{"name":"8","briefIntro":"8","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA73670c3a07ce4259800cbacb1c4aec47","displayOrder":9},{"name":"9","briefIntro":"9","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA11e2f7d8a0574cccb4ab1e8f618ded0a","displayOrder":10}],
        "logoUrl":"/v1/20181206/iGy_0sHpe1B0H9btvRumYQ6a2fedb92f5843258e8e179f2bd6257c",}


    i.add(data,is_sold=True)

    for m in range(3):
        data['param']['name']=m
        data['param']['identityName'] = m
        i.add(data=data,is_sold=True)
        import time
        time.sleep(1)
