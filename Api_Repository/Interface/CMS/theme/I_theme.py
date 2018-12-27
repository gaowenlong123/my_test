from Api_Server.Root.Interface import Interface
import os,requests,copy
from Api_Server.Support.Base_Enums import Enums
from Api_Repository.Data_Center.Entity import *
from Api_Server.Support.Base_Time import *
from Api_Repository.Data_Center.theme import *
from Api_Server.Support.Base_Compare import *

class I_theme(Interface):
    def __init__(self ,para=''):
        super(I_theme ,self).__init__()

        #只新建普通话题，不创建氪友问答
        # 需要跨站展示吗？？ 写上吧

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




    def publish(self ,title,project_id=1 , is_small=True ,is_normal =True):
        '''
        http://cmstest02.36kr.com/api/theme
        :param theme_data:  {'title' }
        :return:
        '''
        _url = self.url + '/theme'
        headers = copy.deepcopy(self.Headers)
        headers['Content-Type'] = 'application/json;charset=UTF-8'
        headers['Cookie'] = headers['Cookie'].split('kr_plus_project_id=')[0] + 'kr_plus_project_id=' + str(project_id)

        if is_normal:
            _data = copy.deepcopy(self.normal_data)
            _data["title"] = get_name(project_id) + title + get_time()
            _data["template_info"] = template_info(title + get_time(), is_small)
        else:
            _data = copy.deepcopy(self.normal_data)
            #氪友问答再说吧

        re =self.request.post(url=_url ,headers=headers ,data=_data)
        # 返回值
        print(re.text)
        try:
            re_dict = {
                'id': re.json()["data"]["id"],
                'title': _data["title"],
                'project_id': project_id
            }
        except:
            re_dict = {}
        return re_dict

    #类拥有的接口
    def recommend(self ,data ,feed=recom_feed.tuijian):
        '''
            http://cmstest02.36kr.com/api/theme/980/recommend
           str : {"recommend_info":"{\"feed_ids\":[269]}"}
           json: recommend_info={"feed_ids":[269]}

           :return {"code":0}
           :type    put
           request
        '''
        if data["project_id"] != 1:
            feed = local_recom_feed(data["project_id"])

        _url=self.url+'/theme/'+str(data["id"])+'/recommend'
        headers = copy.deepcopy(self.Headers)
        headers['Content-Type'] = 'application/json;charset=UTF-8'
        headers['Cookie'] = headers['Cookie'].split('kr_plus_project_id=')[0] + 'kr_plus_project_id=' + str(
            data["project_id"])
        _data = {"recommend_info": feed}

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

    def unhot(self,data):
        '''
        http://cmstest02.36kr.com/api/theme/985/unselect
        :param id:
        :return:
        '''
        _url = self.url + '/theme/' + str(data["id"]) + '/unselect'
        headers = copy.deepcopy(self.Headers)
        headers['Content-Type'] = 'application/json;charset=UTF-8'

        re = self.request.put(url=_url, headers=headers, data={})
        print(re.text)

    def offline(self,data):
        '''
        http://cmstest02.36kr.com/api/theme/983/offline
        :param id:
        :return:
        '''
        _url = self.url + '/theme/'+str(data["id"])+'/offline'
        headers = copy.deepcopy(self.Headers)
        headers['Content-Type'] = 'application/json;charset=UTF-8'

        re=self.request.put(url=_url ,headers=headers,data={})
        print(re.text)

    def top(self,data):
        '''
        http://cmstest02.36kr.com/api/theme/985/stick
        :param id:
        :return:{"code":21000,"msg":"文章非草稿或待审状态，不能删除"}

        {"operate":"no"}    取消置顶
        '''
        _url = self.url + '/theme/' + str(data["id"])+'/stick'
        headers = copy.deepcopy(self.Headers)
        headers['Content-Type'] = 'application/json;charset=UTF-8'
        re = self.request.put(url=_url ,headers=headers,data={"operate":"yes"})
        print(re.text)


    #信息流
    def hot_theme(self):
        '''
        http://test02.36kr.com/pp/api/aggregation-entity?type=selected_theme
        :param id:
        :return:
        '''
        _url = "http://test02.36kr.com/pp/api/aggregation-entity?type=selected_theme"
        re=self.request.get(url= _url )

        try:
            temp = re.json()['data']['items']
        except:
            temp={}
        _list=[]

        for dict in temp:
            s1=map(dict,'title',"无")
            s2=map(dict , 'entity_type' ,"无")
            _list.append(s1+ " : "+ str(s2))
        print("热门话题==>",_list)





if __name__ == '__main__':
    i = I_theme()
    id=i.publish("新建话题" ,project_id=pp_id.chengdu)
    # time.sleep(1)
    # i.recommend({"id":123,"project_id":1})


    # i.offline({"id":986})
    # i.top({"id":986})
    # i.hot({"id":986})

    i.hot_theme()


