from Api_Server.Root.Interface import Interface
import os,requests,copy
from Api_Server.Support.Base_Enums import Enums
from Api_Repository.Data_Center.Entity import *
from Api_Server.Support.Base_Time import *
from Api_Repository.Data_Center.article import *
from Api_Repository.Data_Center.Entity import *
from Api_Server.Support.Base_Compare import *

class I_article(Interface):
    def __init__(self ,para=''):
        super(I_article ,self).__init__()

        #文件新建文章需要的自定义的数据
        # self.article_Data=self.get_post_Data(para)  ??


        #得到文章ID

        self.common_post_data={}


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

    def _public_property(self):
        self.url = 'http://cmstest02.36kr.com/api'
        self.request = requests.session()


    #文章类拥有的接口
    def recommend(self ,data,feed=recom_feed.tuijian):
        '''
            url : http://cmstest02.36kr.com/api/post/10464983/recommend
           str : {"recommend_info":"{\"feed_ids\":[269]}"}
           json: recommend_info={"feed_ids":[269]}

           :return {"code":0}
           :type    put
           request
        '''
        if data["project_id"] !=1:
            feed = local_recom_feed( data["project_id"] )

        _url=self.url+'/post/'+str(data["id"])+'/recommend'
        headers = copy.deepcopy(self.Headers)
        headers['Content-Type'] = 'application/json;charset=UTF-8'
        headers['Cookie'] = headers['Cookie'].split('kr_plus_project_id=')[0] + 'kr_plus_project_id=' + str(data["project_id"])
        _data = {"recommend_info":feed}

        re=self.request.put(url=_url ,headers=headers,data=_data)
        print(re.text)

    def push(self , data ):

        '''
        地方站就先别push了
        :param :data  get 文章的数据
        :return:
        '''
        _url = 'http://cmstest02.36kr.com/api/push'
        headers = copy.deepcopy(self.Headers)
        headers['Content-Type'] = 'application/json;charset=UTF-8'

        ar_post_data={"sound":"1",
                      "title":data['title'],
                      "content":"推送",
                      "entity_type":"post",
                      "entity_id":data['id'],
                      "publish_now":1,
                      "published_at":"",
                      "expire_time":"4"}

        # fl_post_data=

        re=self.request.post(url=_url , headers=self.Headers ,data=ar_post_data)
        print(re.text)

    def review(self,data):
        '''
        http://cmstest02.36kr.com/api/post/10465218/review
        :param data: {'id': 10465323, 'open_at': 1545284393763, 'project_id': 86}
        :return:
        '''
        _url = self.url + '/post/'+str(data["id"])+'/review'
        headers = copy.deepcopy(self.Headers)
        headers['Content-Type'] = 'application/json;charset=UTF-8'
        headers['Cookie'] = headers['Cookie'].split('kr_plus_project_id=')[0] + 'kr_plus_project_id=' + str(
            data["project_id"])

        re=self.request.put(url=_url ,headers=headers,data={})
        print(re.text)

    def delete(self,data):
        '''
        http://cmstest02.36kr.com/api/post/10465214
        :param id:
        :return:{"code":21000,"msg":"文章非草稿或待审状态，不能删除"}
        '''
        _url = self.url + '/post/' + str(data["id"])
        headers = copy.deepcopy(self.Headers)
        headers['Content-Type'] = 'application/json;charset=UTF-8'
        headers['Cookie'] = headers['Cookie'].split('kr_plus_project_id=')[0] + 'kr_plus_project_id=' + str(
            data["project_id"])

        re = self.request.delete(url=_url ,headers=headers,data={})
        print(re.text)

    def republish(self ,data):
        '''
        http://cmstest01.36kr.com/api/post/10465235/publish
        :param id:
        :return:{"code":0}
        '''
        _url = self.url + '/post/' + str(data["id"])+'/publish'
        headers = copy.deepcopy(self.Headers)
        headers['Content-Type'] = 'application/json;charset=UTF-8'
        headers['Cookie'] = headers['Cookie'].split('kr_plus_project_id=')[0] + 'kr_plus_project_id=' + str(
            data["project_id"])

        re = self.request.put(url=_url, headers=headers, data={})
        print(re.text)


    #聚合发布文章
    def creat_publish(self, title, project_id=1, publish=0):
        data = self.get_ID(title)

        article_data = self.get_article_data(data=data)

        post_data = self.Cmod_article(article_data=article_data, data=data)

        self.publish(post_data, data=data)

        return data
    def creat_publish_recom(self, title):
        data = self.get_ID(title)

        article_data = self.get_article_data(data=data)

        post_data = self.Cmod_article(article_data=article_data, data=data)

        self.publish(post_data, data=data)

        time.sleep(1)

        self.recommend(data)

        return data

    # 发布文章流程
    def get_ID(self , title='',project_id=1 ,publish=0):
        '''
          #添加文章
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
        temp_dict={}

        headers['Content-Type'] = 'application/json;charset=UTF-8'
        headers['Cookie']=headers['Cookie'].split('kr_plus_project_id=')[0]+'kr_plus_project_id='+str(project_id)
        template = "{\"template_type\":\"small_image\",\"template_title\":\""+title+"\",\"template_title_isSame\":true,\"template_cover\":[]}"

        post_data={"title": title + get_time(),
                   "column_id":"",
                   "source_type":"original",
                   "user_id":12186523,
                   "source_urls":"",
                   "content":"",
                   "template_info":template }

        re=self.request.post(url=_url ,data=post_data ,headers=headers)

        try:
            temp_dict = re.json()["data"]
        except KeyError:
            print(re.text)
            assert "报错"

        if publish !=0:
            temp_dict.update({"published_at": get_late_time(publish)})
            temp_dict.update({"publish_now": 0})
        temp_dict.update({"project_id":project_id})
        print(temp_dict)
        return temp_dict

    def get_article_data(self ,data):
        '''
        :param data:
        :project_id : 1 主站
        :return: kr_plus_project_id=86

        '''
        _url='http://cmstest02.36kr.com/api/post/'+str(data["id"])+'?open_in_editor=1'  #&_=1544607271040
        headers = copy.deepcopy(self.Headers)
        headers['Cookie']=headers['Cookie'].split('kr_plus_project_id=')[0]+'kr_plus_project_id='+str(data["project_id"])

        re=self.request.get(url=_url ,headers=headers)
        print(re.text)
        common_post_data=re.json()

        print('模板文章 ====>> ' ,common_post_data['data'])
        return common_post_data['data']

    def Cmod_article(self ,article_data ,data):
        '''
        :param article_data:  模板信息
        :param mod_data:      需要修改的字典
        :return:
        '''
        _url = 'http://cmstest02.36kr.com/api/post/' + str(article_data['id'])
        headers = copy.deepcopy(self.Headers)
        headers['Content-Type'] = 'application/json;charset=UTF-8'
        headers['Cookie'] = headers['Cookie'].split('kr_plus_project_id=')[0] + 'kr_plus_project_id=' + str(
            data["project_id"])

        mod_data={
            "template_info": template_info(article_data['title'],0) ,
	        "summary": summary.sum,
	        "content": content.dada,
	        "cover": ramdom_cover(),
	        "created_at":get_time(),
	        "updated_at":get_time() ,
	        "report_type": report_type.chuang,
	        "motifs":motifs.one ,
	        "last_open_at":str(time_Stamp())
        }

        for dict in mod_data:
            article_data[dict]=mod_data[dict]

        print(article_data)

        re = self.request.put(url=_url, headers=headers, data=article_data)
        print(re.text)

        return article_data

    def publish(self ,article_data ,data):
        ''''''
        _url = 'http://cmstest02.36kr.com/api/post/'+str(article_data["id"])+'/publish'
        headers = copy.deepcopy(self.Headers)
        headers['Content-Type'] = 'application/json;charset=UTF-8'
        headers['Cookie'] = headers['Cookie'].split('kr_plus_project_id=')[0] + 'kr_plus_project_id=' + str(
            data["project_id"])

        if data.get("publish_now",None)==None:
            article_data.update({"publish_now":1})
        else:
            article_data["published_at"]=data["published_at"]
            article_data["publish_now"] =data["publish_now"]

        re =self.request.put(url=_url ,headers=headers ,data=article_data)
        print(re.text)

    def my_offline_delete(self):
        '''
        http://cmstest02.36kr.com/api/post?user_id=12186523&per_page=40&page=1
        :return:
        '''
        _url = 'http://cmstest02.36kr.com/api/post?user_id=12186523&per_page=40&page=1'
        headers = copy.deepcopy(self.Headers)
        _temp =[]
        re=self.request.get(url=_url ,headers=headers)
        _list=re.json()["data"]["data"]

        for dict in _list:
            _temp.append(map(dict ,"id" ,0))

        print(_temp)

        for id in _temp:
            if id !=0:
                self.review({"id":id ,"project_id":1})
                time.sleep(1)
                self.delete({"id":id ,"project_id":1})
                time.sleep(1)

    #???
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

    title='测试发布文章'
    temp=[]
    # for m in range(0):
    #     data=i.get_ID(title)
    #     print(data)
    #     article_data=i.get_article_data(data=data)
    #
    #     post_data=i.Cmod_article(article_data=article_data ,data=data)
    #
    #     i.publish(post_data ,data=data)
        #
        # time.sleep(1)
        #
        # i.recommend(data)
        #
        # temp.append(data['id'])

    # i.push(post_data)
    print(temp)

    # i.review({"id":10465256 ,"project_id":1})
    # i.my_offline_delete()








