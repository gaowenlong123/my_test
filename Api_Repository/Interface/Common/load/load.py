class Common():

    #放到通用文件里面
    def upload(self ,headers ,request,data=''):
        '''                        搞不定 ，编码搞不定  ，看后期是路径还是压缩编码

        http://assisttest31.36kr.com/api/oss/upload
        :return: path
        '''
        headers['Content-Type']= 'multipart/form-data; boundary=----WebKitFormBoundaryanBjBj5Hd04jXAYG'
        print(headers)
        url = 'http://assisttest31.36kr.com/api/oss/upload'
        from Api_Server.Base.Base_Data import read_text_by_gbk
        data= read_text_by_gbk('E:\Pycharm_Git\my_test\Picture\a.html')
        # data=str(data)
        print(type(data))
        re=request.post(url=url,data=data ,headers=headers)
        print(re.text)

        return 'path 路径'

    def common_photo(self,id,url):
        '''
        :data :
        :param id:
        :param url:
        :return:
        '''
        _url = 'http://cmstest02.36kr.com/api/photo-hidden'
        headers = copy.deepcopy(self.Headers)
        headers['Content-Type'] = 'application/json;charset=UTF-8'

        photo="[{"+url+"}]"
        post_data={"entity_id": id,
                   "entity_type": "post",
                    "list": photo}

        re=self.request.post(url=_url ,headers=headers ,data=post_data)
        print(re.text)
