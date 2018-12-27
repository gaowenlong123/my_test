
from Api_Server.Root.Interface import Interface
from Api_Server.Support.Base_Time import *
from Api_Repository.Data_Center.monographic import *
from Api_Server.Support.Base_Enums import Enums
import copy , requests ,os
from Api_Repository.Data_Center.Entity import *
class I_monographic(Interface):
    def __init__(self ,param = ''):
        super(I_monographic ,self).__init__()

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
        self._url='http://cmstest02.36kr.com/api'

        self.request = requests.session()

        #
        self.post_data = {"cover":"",
                          "cover_web":"",
                          "summary":"摘要",
                          "title":"",
                          "type":"advertisement", #这个先这样
                          "list":"",
                          "template_info":"",
                          "published_at":"",
                          "publish_now":1}


    def publish(self,title ,project_id=1 ,type=0 ,publish_time=0):
        headers = copy.deepcopy(self.Headers)
        _data = copy.deepcopy(self.post_data)
        headers['Content-Type'] = 'application/json;charset=UTF-8'
        headers['Cookie'] = headers['Cookie'].split('kr_plus_project_id=')[0] + 'kr_plus_project_id=' + str(project_id)

        _data["title"] = get_name(project_id) + title + get_time()
        _data["cover_web"] =web_cover.W
        _data["cover"] = cover.A
        _data["list"] = list.list
        _data["template_info"] = template_info(_data["title"] ,type)     #选择模板

        if publish_time != 0 :
            _data["published_at"] = get_late_time(publish_time)
            _data["publish_now"] = 0

        re =self.request.post(url=self._url + '/monographic' , headers=headers ,data=_data)
        print(re.text)

        # 返回值
        try:
            re_dict = {
                'id': re.json()["data"]["id"],
                'title': _data["title"],
                'project_id': project_id
            }
        except:
            re_dict = {}
        print(re_dict)
        return re_dict

    def recommend(self, data, feed=recom_feed.tuijian):

        if data["project_id"] != 1:
            feed = local_recom_feed(data["project_id"])

        _url = self._url + '/monographic/' + str(data["id"]) + '/recommend'
        headers = copy.deepcopy(self.Headers)
        headers['Content-Type'] = 'application/json;charset=UTF-8'
        headers['Cookie'] = headers['Cookie'].split('kr_plus_project_id=')[0] + 'kr_plus_project_id=' + str(
            data["project_id"])
        _data = {"recommend_info": feed}

        re = self.request.put(url=_url, headers=headers, data=_data)
        print(re.text)


    def review(self,data):

        _url = self._url + '/monographic/'+str(data["id"])+'/review'
        headers = copy.deepcopy(self.Headers)
        headers['Content-Type'] = 'application/json;charset=UTF-8'
        headers['Cookie'] = headers['Cookie'].split('kr_plus_project_id=')[0] + 'kr_plus_project_id=' + str(
            data["project_id"])

        re=self.request.put(url=_url ,headers=headers,data={})
        print(re.text)

    def top(self):
        '''  置顶先不做'''
        pass

if __name__ == '__main__':

    i = I_monographic()
    i.publish("测试发布专题" ,type=1 ,publish_time=4 ,project_id=pp_id.xiamen)
    # i.recommend({'id': 814,  'project_id': 1})
    # i.review({'id': 814,  'project_id': 1})