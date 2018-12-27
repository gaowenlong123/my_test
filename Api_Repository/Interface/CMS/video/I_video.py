from Api_Server.Root.Interface import Interface
from Api_Server.Support.Base_Enums import Enums
from Api_Server.Support.Base_Time import *
from Api_Repository.Data_Center.video import *
from Api_Repository.Data_Center.Entity import *
import os ,copy ,requests,json


class I_video(Interface):
    def __init__(self):
        super(I_video,self).__init__()



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
        # 显示标题 ，外链
        self.post_data = {"user_id":12186523,
                          "title":"",
                          "vtype":"normal",
                          "column_id":"",
                          "video_values":"",
                          "label_ids":[],
                          "template_info":"{\"template_type\":\"big_image\",\"template_title\":\"测试视频大图\",\"template_title_isSame\":true,\"template_cover\":[]}",
                          "state":"drafted"}


        self.url = 'http://cmstest02.36kr.com/api/video'

        self.request=requests.session()

    def create_publish(self ,title ,project_id =1,pulish_time=0 ):
        data = self.get_Id(title, project_id=project_id, pulish_time=pulish_time)
        self.Cmod_video(data)
        self.publish(data)

    def create_publish_recom(self, title, project_id=1):
        data = self.get_Id(title, project_id=project_id)
        self.Cmod_video(data)
        self.publish(data)
        time.sleep(1)
        self.recommend(data)


    #发布视频流程
    def get_Id(self ,title  ,pulish_time=0 ,project_id=1):
        '''

        data=
        :param title:
        :return:  {"code":0,"msg":"","data":{"id":2976}}
        '''
        headers = copy.deepcopy(self.Headers)
        _data = copy.deepcopy(self.post_data)
        temp_dict = {}

        headers['Content-Type'] = 'application/json;charset=UTF-8'
        headers['Cookie'] = headers['Cookie'].split('kr_plus_project_id=')[0] + 'kr_plus_project_id=' + str(project_id)

        _data["title"]=get_name(project_id)+title+get_time()

        re = self.request.post(url=self.url, data=json.dumps(_data), headers=headers)
        try:
            temp_dict = re.json()["data"]
        except KeyError:
            print(re.text)
            assert "报错"
        temp_dict.update({"project_id":project_id})
        temp_dict.update({"title": _data["title"]})
        if pulish_time ==0:
            temp_dict.update({"published_at":""})
        else:
            temp_dict.update({"published_at": get_late_time(pulish_time)})

        print(temp_dict)
        return temp_dict


    def Cmod_video(self, video_data):
        '''
        也可以用作更改信息
        :param article_data:  模板信息
        :param mod_data:      需要修改的字典
        :return:
        '''
        _url = 'http://cmstest02.36kr.com/api/video/' + str(video_data['id'])
        headers = copy.deepcopy(self.Headers)
        _data = copy.deepcopy(self.post_data)
        headers['Content-Type'] = 'application/json;charset=UTF-8'
        headers['Cookie'] = headers['Cookie'].split('kr_plus_project_id=')[0] + 'kr_plus_project_id=' + str(
            video_data["project_id"])

        _data= {"user_id": "12186523",
             "title": video_data["title"],
             "summary": "视频简介",
             "vtype": "normal",
             "web_cover":web_cover.one,
            "column_id":"",
            "video_values":video_values.one,
            "label_ids": [],
            "cover":cover.one,
            "template_info":template_info(video_data["title"]),
            "publish_now": 1,
            "published_at": video_data["published_at"]
        }

        re = self.request.put(url=_url, headers=headers, data=json.dumps(_data))
        print(re.text)
        print(video_data)
        return video_data

    def publish(self, video_data):
        ''''''
        _url = 'http://cmstest02.36kr.com/api/video/' + str(video_data["id"]) + '/publish'
        headers = copy.deepcopy(self.Headers)
        headers['Content-Type'] = 'application/json;charset=UTF-8'
        headers['Cookie'] = headers['Cookie'].split('kr_plus_project_id=')[0] + 'kr_plus_project_id=' + str(
            video_data["project_id"])

        if video_data["published_at"] == "":
            _data={"published_at":"","publish_now":1}
        else:
            _data={"published_at":video_data["published_at"],"publish_now":0}

        re = self.request.put(url=_url, headers=headers, data=json.dumps(_data))
        print(re.text)

    def recommend(self, data, feed=recom_feed.tuijian):
        '''
            url : http://cmstest02.36kr.com/api/post/10464983/recommend
           str : {"recommend_info":"{\"feed_ids\":[269]}"}
           json: recommend_info={"feed_ids":[269]}

           :return {"code":0}
           :type    put
           request
        '''
        if data["project_id"] != 1:
            feed = local_recom_feed(data["project_id"])

        _url = self.url+'/'+ str(data["id"]) + '/recommend'
        headers = copy.deepcopy(self.Headers)
        headers['Content-Type'] = 'application/json;charset=UTF-8'
        headers['Cookie'] = headers['Cookie'].split('kr_plus_project_id=')[0] + 'kr_plus_project_id=' + str(
            data["project_id"])
        _data = {"recommend_info": feed}

        re = self.request.put(url=_url, headers=headers, data=_data)
        print(re.text)

    def offline(self,data):
        '''
        http://cmstest02.36kr.com/api/video/2992/offline
        :param data:  #跨品牌下线
        :return:
        '''
        _url = 'http://cmstest02.36kr.com/api/video/' + str(data['id'])+'/offline'
        headers = copy.deepcopy(self.Headers)

        if data.get("project_id" ,None) ==None:
            data["project_id"]=1

        headers['Content-Type'] = 'application/json;charset=UTF-8'
        headers['Cookie'] = headers['Cookie'].split('kr_plus_project_id=')[0] + 'kr_plus_project_id=' + str(
            data["project_id"])

        re=self.request.put(url=_url ,headers=headers,data={})
        print(re.text)

if __name__ == '__main__':

    i = I_video()
    # i.create_publish("测试发布视频",project_id=pp_id.fuzhou ,pulish_time=2)
    i.create_publish_recom("测试推荐视频", project_id=pp_id.fuzhou)

    # i.offline({"id":2993})
