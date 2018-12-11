from Base.Root.Interface import Interface
import os,requests,copy ,json
from Base.Support.Base_Enums import Enums
from Picture.Picture import CMS_Picture


class I_article(Interface):
    def __init__(self ,para=''):
        super(I_article ,self).__init__()

        #文件新建文章需要的自定义的数据
        # self.article_Data=self.get_post_Data(para)  ??

        self.url = 'http://cmstest02.36kr.com/api'
        self.request = requests.session()
        #得到文章ID




  #重写虚方法
    def get_dir_name(self):
        '''
          #必须重新，获得该文件夹名，生成存储文件
        :return: dir_name
        '''
        dir_name=str(os.path.dirname(__file__).split('/')[-1])
        return dir_name

    def get_post_Data(self , para):
        '''
        得到输入的参数，拼接生成可以发送请求的文章参数
        :return: 可以提交的文章的结构体
        '''
        pass


    def get_url(self):
        return Enums.test_Cms_url




    #文章类的基本属性  （1:自己定义的标题、图片等，可以随时改变， 2：系统提供的属性，创建时间等等，不可直接更改的（1：不能更改的 2：可以通过系统事件来更改的）那么就是只读吧


    #文章的基本方法
    def get_dict(self):
        '''
        将得到的对象，转成字典
        :return: dict
        '''
        pass


    #文章类拥有的接口
    def recommend(self ,id):
        '''
            url : http://cmstest02.36kr.com/api/post/10464983/recommend
           str : {"recommend_info":"{\"feed_ids\":[269]}"}
           json: recommend_info={"feed_ids":[269]}

           :return {"code":0}
           :type    put
           request
Host: cmstest02.36kr.com
Connection: keep-alive
Content-Length: 41
Accept: */*
Origin: http://cmstest02.36kr.com
x-requested-with: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36
Content-Type: application/json
Referer: http://cmstest02.36kr.com/posts
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: .....
       '''

    def get_ID(self , title=''):
        '''
        :url   :  /post
        :data :
         {"title":"测试配图-小图",
        "column_id":"",
        "source_type":"original",
        "user_id":12186523,
        "source_urls":"",
        "content":"",
        "template_info":"{\"template_type\":\"small_image\",\"template_title\":\"测试配图-小图\",\"template_title_isSame\":true,\"template_cover\":[]}"}

        在编辑页面的提交文章标题时，会生成文章ID
        :return:  文章的ID
        '''
        headers = copy.deepcopy(self.Headers)
        _url = self.url + '/post'

        headers['Content-Type'] = 'application/json;charset=UTF-8'

        post_data={"title": title,
                   "column_id":"",
                   "source_type":"original",
                   "user_id":12186523,
                   "source_urls":"",
                   "content":"",
                   "template_info":"{\"template_type\":\"small_image\","
                                   "\"template_title\":\"测试配图-小图\","
                                   "\"template_title_isSame\":true,"
                                   "\"template_cover\":[]}"}
        pass

        re=self.request.post(url=_url ,data=post_data ,headers=headers)
        print(re.json())

        return re.json()["data"]["id"]

    #丰富文章实体
    def create_article(self ,id):
        ''''''
        _url='http://cmstest02.36kr.com/api/post/'+str(id)
        headers = copy.deepcopy(self.Headers)
        headers['Content-Type'] = 'application/json;charset=UTF-8'

        post_data={"id":id,
                   "project_id":"1",
                   "monographic_id":"0",
                   "column_id":"",
                   "is_tovc":"0",
                   "goods_id":"0",
                   "domain_id":"0",
                   "is_free":"0",
                   "related_company_id":"0",
                   "company_id":"0",
                   "related_company_type":"domestic",
                   "related_company_name":"",
                   "total_words":"9",
                   "close_comment":"0",
                   "has_audio":"0",
                   "state":"drafted",
                   "recommend_info":null,
                   "entity_flag":null,
                   "template_info":"{\"template_type\":\"small_image\",\"template_title\":\"测试配图-小图\",\"template_title_isSame\":true,\"template_cover\":[\"https://pic.36krcnd.com/201812/11045923/85a7hciqiu6rizft\"]}",
                   "stat_belong":"",
                   "title":"测试配图-小图",
                   "title_mobile":null,
                   "catch_title":"",
                   "summary":"文章摘要11",
                   "content":"<p>勿删，不要删啊啊啊</p><p><br/></p>",
                   "remark":null,
                   "slug":"",
                   "cover":"https://pic.36krcnd.com/201812/11051635/xqqqybmru90k2xfu",
                   "cover_mobile":null,
                   "source_type":"original",
                   "source_urls":"",
                   "related_post_ids":"",
                   "key":"",
                   "extra":null,
                   "user_id_old":null,
                   "user_id":"12186523",
                   "user_id_edited_old":null,
                   "user_id_edited":"12186523",
                   "user_id_created":"12186523",
                   "user_id_tagged":null,
                   "views_count":"0",
                   "mobile_views_count":"0",
                   "app_views_count":"0",
                   "edited_at":"2018-12-11 14:07:52",
                   "published_at":null,
                   "created_at":"2018-12-11 12:23:38",
                   "updated_at":"2018-12-11 14:07:52",
                   "pin":"0","pushed_at":null,
                   "report_type":"港股观察",
                   "user":{"id":"12186523",
                           "avatar_url":"/static/avatar.d864db3e.png",
                           "name":"自动化小能手",
                           "nickname":"自动化小能手",
                           "realname":null,
                           "email":null,
                           "crm_email":null,
                           "title":"读者",
                           "department_belong":"",
                           "introduction":"",
                           "is_author":"1"},
                   "column":null,
                   "audios":[],
                   "domain":{"id":"0",
                             "name":"测试领域推送",
                             "cover":null,
                             "user_id":"0",
                             "user_id_edited":"0",
                             "created_at":null,
                             "updated_at":null},
                   "post_tovc":null,
                   "motifs":[],
                   "open_at":"1544508522829",
                   "audio_ids":"",
                   "last_open_at":"1544508522829"}

        re=self.request.put(url=_url , headers=headers ,data=post_data)
        print(re.text)

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

    def calculate_motif(self , id ):

        _url ='http://cmstest02.36kr.com/api/post/'+str(id)+'/calculate-motif '

        headers = copy.deepcopy(self.Headers)
        headers['Content-Type'] = 'application/json;charset=UTF-8'
        post_data ={}

        re=self.request.post(url=_url , headers=headers ,data=post_data)
        print(re.text)

    def publish(self ,title, data ,):
        ''''''
        _url = 'http://cmstest02.36kr.com/api/post/'+str(id)+'/publish'
        headers = copy.deepcopy(self.Headers)
        headers['Content-Type'] = 'application/json;charset=UTF-8'

        template_info ='标题怎么办'

        post_data ={"id":data["id"],
                    "open_at":data["open_at"],
                    "state":"drafted",
                    "project_id":"1",
                    "monographic_id":"0",
                    "column_id":"",
                    "is_tovc":"0",
                    "goods_id":"0",
                    "domain_id":"0",
                    "is_free":"0",
                    "related_company_id":"0",
                    "company_id":"0",
                    "related_company_type":"domestic",
                    "related_company_name":"",
                    "total_words":"0",
                    "close_comment":"0",
                    "has_audio":"0",
                    "recommend_info":null,
                    "entity_flag":null,
                    "template_info":"{\"template_type\":\"small_image\",\"template_title\":\"融资-测试关键字\",\"template_title_isSame\":true,\"template_cover\":[\"https://pic.36krcnd.com/201812/11090658/yidycxipnetj6sap\"]}",
                    "stat_belong":"",
                    "title":"融资-测试关键字",
                    "title_mobile":null,
                    "catch_title":"",
                    "summary":"防守打法",
                    "content":"<p>哈哈关键字哈哈</p>",
                    "remark":null,
                    "slug":"",
                    "cover":"https://pic.36krcnd.com/201812/11090708/v0ch4zbcpd6mh26q",
                    "cover_mobile":null,
                    "source_type":"original",
                    "source_urls":"",
                    "related_post_ids":"",
                    "key":"",
                    "extra":null,
                    "user_id_old":null,
                    "user_id":"12186523",
                    "user_id_edited_old":null,
                    "user_id_edited":"12186523",
                    "user_id_created":"12186523",
                    "user_id_tagged":null,
                    "views_count":"0",
                    "mobile_views_count":"0",
                    "app_views_count":"0",
                    "edited_at":null,
                    "published_at":"",
                    "created_at":"2018-12-11 17:05:43",
                    "updated_at":"2018-12-11 17:05:43",
                    "pin":"0",
                    "pushed_at":null,
                    "report_type":"港股观察",
                    "user":{"id":"12186523","avatar_url":"/static/avatar.d864db3e.png","name":"自动化小能手","nickname":"自动化小能手","realname":null,"email":null,"crm_email":null,"title":"读者","department_belong":"","introduction":"","is_author":"1"},
                    "column":null,
                    "audios":[],
                    "domain":{"id":"0","name":"测试领域推送","cover":null,"user_id":"0","user_id_edited":"0","created_at":null,"updated_at":null},
                    "post_tovc":null,
                    "motifs":[],
                    "audio_ids":"",
                    "last_open_at":"1544519144402",       #时间戳
                    "motif_ids":[],                       #主题  ["340"]
                    "publish_now":1
                    }

        san_data={"id":"10465097",
                  "open_at":"1544510671716",
                  "state":"drafted",
                  "project_id":"1",
                  "monographic_id":"0",
                  "column_id":"",
                  "is_tovc":"0",
                  "goods_id":"0",
                  "domain_id":"0",
                  "is_free":"0",
                  "related_company_id":"0",
                  "company_id":"0",
                  "related_company_type":"domestic",
                  "related_company_name":"",
                  "total_words":"0",
                  "close_comment":"0",
                  "has_audio":"0",
                  "recommend_info":null,
                  "entity_flag":null,
                  "template_info":"{\"template_type\":\"multi_image\",\"template_title\":\"测试配图-三图\",\"template_title_isSame\":true,\"template_cover\":[\"https://pic.36krcnd.com/201812/11065244/lkkcikdrcuoai9k5\",\"https://pic.36krcnd.com/201812/11065251/xssz1apxcakog2jq\",\"https://pic.36krcnd.com/201812/11065302/sfubsvx52cz84zt9\"]}",
                  "stat_belong":"",
                  "title":"测试配图-三图",
                  "title_mobile":null,
                  "catch_title":"",
                  "summary":"文章摘要",
                  "content":"<p>勿删<br/></p>",
                  "remark":null,
                  "slug":"",
                  "cover":"https://pic.36krcnd.com/201812/11065313/0rhymj7c7sj7a6un",
                  "cover_mobile":null,
                  "source_type":"original",
                  "source_urls":"",
                  "related_post_ids":"",
                  "key":"",
                  "extra":null,
                  "user_id_old":null,
                  "user_id":"12186523",
                  "user_id_edited_old":null,
                  "user_id_edited":"12186523",
                  "user_id_created":"12186523",
                  "user_id_tagged":null,
                  "views_count":"0",
                  "mobile_views_count":"0",
                  "app_views_count":"0",
                  "edited_at":null,
                  "published_at":"",
                  "created_at":"2018-12-11 14:44:30",
                  "updated_at":"2018-12-11 14:44:30",
                  "pin":"0",
                  "pushed_at":null,
                  "report_type":"港股观察",
                  "user":{"id":"12186523",
                          "avatar_url":"/static/avatar.d864db3e.png",
                          "name":"自动化小能手",
                          "nickname":"自动化小能手",
                          "realname":null,
                          "email":null,
                          "crm_email":null,
                          "title":"读者",
                          "department_belong":"",
                          "introduction":"",
                          "is_author":"1"},
                  "column":null,
                  "audios":[],
                  "domain":{"id":"0",
                            "name":"测试领域推送",
                            "cover":null,
                            "user_id":"0",
                            "user_id_edited":"0",
                            "created_at":null,
                            "updated_at":null},
                  "post_tovc":null,
                  "motifs":[],
                  "audio_ids":"",
                  "last_open_at":"1544510671716",
                  "motif_ids":["340"],
                  "publish_now":1}

        re =self.request.put(url=_url ,headers=headers ,data=post_data)
        print(re.text)


if __name__ == '__main__':
    #例
    i=I_article()

    #写入text
    # for i1 in range(10):
    #     i.write('21111sssssssssss我是文章1dadwaa')
    # i.write('adada')
    #
    # #写入dict
    # b={"aaaa":111,"22":222222}
    # c={'dada':222444}
    # i.write_dict(b)
    # i.write_dict(c)
    # i.end_write(is_clear=False)   #将存的字典写入text中 ,不删除文件
    #
    # print(i.Headers)


    id=i.get_ID('hshshsshhshhh')
    i.common_photo(id ,CMS_Picture.xiao )
    i.common_photo(id ,CMS_Picture.web)
    i.calculate_motif(id)

    again_post = {"id": "10465100",
                  "open_at": "1544519144402",
                  "state": "drafted",
                  "project_id": "1",
                  "monographic_id": "0",
                  "column_id": "",
                  "is_tovc": "0",
                  "goods_id": "0",
                  "domain_id": "0",
                  "is_free": "0",
                  "related_company_id": "0",
                  "company_id": "0",
                  "related_company_type": "domestic",
                  "related_company_name": "",
                  "total_words": "0",
                  "close_comment": "0",
                  "has_audio": "0",
                  "recommend_info": null,
                  "entity_flag": null,
                  "template_info": "{\"template_type\":\"small_image\",\"template_title\":\"融资-测试关键字\",\"template_title_isSame\":true,\"template_cover\":[\"https://pic.36krcnd.com/201812/11090658/yidycxipnetj6sap\"]}",
                  "stat_belong": "",
                  "title": "融资-测试关键字",
                  "title_mobile": null,
                  "catch_title": "",
                  "summary": "防守打法",
                  "content": "<p>哈哈关键字哈哈</p>",
                  "remark": null,
                  "slug": "",
                  "cover": "https://pic.36krcnd.com/201812/11090708/v0ch4zbcpd6mh26q",
                  "cover_mobile": null,
                  "source_type": "original",
                  "source_urls": "",
                  "related_post_ids": "",
                  "key": "",
                  "extra": null,
                  "user_id_old": null,
                  "user_id": "12186523",
                  "user_id_edited_old": null,
                  "user_id_edited": "12186523",
                  "user_id_created": "12186523",
                  "user_id_tagged": null,
                  "views_count": "0",
                  "mobile_views_count": "0",
                  "app_views_count": "0",
                  "edited_at": null,
                  "published_at": null,
                  "created_at": "2018-12-11 17:05:43",
                  "updated_at": "2018-12-11 17:05:43",
                  "pin": "0", "pushed_at": null,
                  "report_type": "港股观察",
                  "user": {"id": "12186523",
                           "avatar_url": "/static/avatar.d864db3e.png",
                           "name": "自动化小能手",
                           "nickname": "自动化小能手",
                           "realname": null,
                           "email": null,
                           "crm_email": null,
                           "title": "读者",
                           "department_belong": "",
                           "introduction": "",
                           "is_author": "1"},
                  "column": null,
                  "audios": [],
                  "domain": {"id": "0",
                             "name": "测试领域推送",
                             "cover": null,
                             "user_id": "0",
                             "user_id_edited": "0",
                             "created_at": null,
                             "updated_at": null},
                  "post_tovc": null,
                  "motifs": [],
                  "audio_ids": "",
                  "last_open_at": "1544519144402"}
