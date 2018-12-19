from Api_Server.Root.Interface import Interface
import os,requests,copy
from Api_Server.Support.Base_Enums import Enums,recom_feed
from Api_Server.Support.Base_Time import *
from Api_Repository.Data_Center.theme import *


class I_theme(Interface):
    def __init__(self ,para=''):
        super(I_theme ,self).__init__()

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

        self.normal_data={"title":"",
                      "column_id":"",
                      "description":"话题描述",
                      "cover":"",
                      "discover_cover":"https://pic.36krcnd.com/201812/11070237/vn5xbd24saqxoy8n",
                      "short_title":"话题简称",
                      "type":"0",
                      "template_info":"",
                      "publish_now":1,
                      "published_at":"",
                      "category":"normal"}

        self.keyouwenda_data={}


    #章类拥有的接口
    def recommend(self ,id):
        '''
            http://cmstest02.36kr.com/api/theme/980/recommend
           str : {"recommend_info":"{\"feed_ids\":[269]}"}
           json: recommend_info={"feed_ids":[269]}

           :return {"code":0}
           :type    put
           request
        '''
        _url=self.url+'/theme/'+str(id)+'/recommend'
        headers = copy.deepcopy(self.Headers)
        headers['Content-Type'] = 'application/json;charset=UTF-8'
        _data = {"recommend_info":recom_feed.tuijian}

        re=self.request.put(url=_url ,headers=headers,data=_data)
        print(re.text)

    def hot(self,id):
        '''
        http://cmstest02.36kr.com/api/theme/985/select
        :param id:
        :return:
        '''
        _url = self.url + '/theme/' + str(id) + '/select'
        headers = copy.deepcopy(self.Headers)
        headers['Content-Type'] = 'application/json;charset=UTF-8'

        re = self.request.put(url=_url, headers=headers, data={})
        print(re.text)

    def unhot(self,id):
        '''
        http://cmstest02.36kr.com/api/theme/985/unselect
        :param id:
        :return:
        '''
        _url = self.url + '/theme/' + str(id) + '/unselect'
        headers = copy.deepcopy(self.Headers)
        headers['Content-Type'] = 'application/json;charset=UTF-8'

        re = self.request.put(url=_url, headers=headers, data={})
        print(re.text)

    def offline(self,id):
        '''
        http://cmstest02.36kr.com/api/theme/983/offline
        :param id:
        :return:
        '''
        _url = self.url + '/theme/'+str(id)+'/offline'
        headers = copy.deepcopy(self.Headers)
        headers['Content-Type'] = 'application/json;charset=UTF-8'

        re=self.request.put(url=_url ,headers=headers,data={})
        print(re.text)

    def top(self,id):
        '''
        http://cmstest02.36kr.com/api/theme/985/stick
        :param id:
        :return:{"code":21000,"msg":"文章非草稿或待审状态，不能删除"}

        {"operate":"no"}    取消置顶
        '''
        _url = self.url + '/theme/' + str(id)+'/stick'
        headers = copy.deepcopy(self.Headers)
        headers['Content-Type'] = 'application/json;charset=UTF-8'
        re = self.request.put(url=_url ,headers=headers,data={"operate":"yes"})
        print(re.text)

    def publish(self ,title,is_small=True ,is_normal =True):
        '''
        http://cmstest02.36kr.com/api/theme
        :param theme_data:  {'title' }
        :return:
        '''
        _url = self.url + '/theme'
        headers = copy.deepcopy(self.Headers)
        headers['Content-Type'] = 'application/json;charset=UTF-8'

        if is_normal:
            _data = copy.deepcopy(self.normal_data)
            _data["title"] = title + get_time()
            _data["template_info"] = template_info(title + get_time(), is_small)
        else:
            _data = copy.deepcopy(self.normal_data)
            #氪友问答再说吧

        re =self.request.post(url=_url ,headers=headers ,data=_data)
        print(re.json()['data'])

        return re.json()['data']['id']

    #信息流
    def hot_theme(self,id):
        '''
        http://test02.36kr.com/pp/api/aggregation-entity?type=selected_theme
        :param id:
        :return:
        '''


    #????
    def push(self , data ):

        '''
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


if __name__ == '__main__':
    i = I_theme()
    # id=i.publish("新建话题")
    # time.sleep(1)
    # i.recommend(id)

    # i.offline(986)
    # i.top(984)


    i.hot()