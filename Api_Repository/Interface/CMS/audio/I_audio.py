from Api_Server.Root.Interface import Interface
from Api_Server.Support.Base_Time import *
from Api_Repository.Data_Center.newsflash import *
from Api_Server.Support.Base_Enums import Enums
import copy , requests ,os ,json
from Api_Repository.Data_Center.audio import *

class I_audio(Interface):
    def __init__(self ,param = ''):
        super(I_audio ,self).__init__()

        self.request = requests.session()



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
        self.url='http://cmstest02.36kr.com/api'

        #
        self._data = {"user_id":12186523,
                          "title":"",
                          "column_id":"",
                          "audio_values":"",
                          "template_info":"",
                          "state":"drafted"
                          }



    def get_id(self,title,project_id=1):
        '''
        http://cmstest02.36kr.com/api/audio
        :param title:
        :return:
        '''
        _url = self.url +'/audio'
        headers = copy.deepcopy(self.Headers)
        _data = copy.deepcopy(self._data)
        headers['Content-Type'] = 'application/json;charset=UTF-8'
        headers['Cookie'] = headers['Cookie'].split('kr_plus_project_id=')[0] + 'kr_plus_project_id=' + str(project_id)

        _data["title"] = title + get_time()
        _data["template_info"]=template_info(title)

        re= self.request.post(url=_url ,data=_data,headers=headers)

        # 返回值
        re_dict = {
            'id': re.json()["data"]["id"],
            'title': _data["title"],
            'project_id': project_id
        }
        print(re_dict)
        return re_dict


    def Cmod_audio(self, audio_data):
        '''
        也可以用作更改信息
        :param article_data:  模板信息
        :param mod_data:      需要修改的字典
        :return:
        '''
        _url = self.url +'/audio/' + str(audio_data['id'])
        headers = copy.deepcopy(self.Headers)
        _data = copy.deepcopy(self._data)
        headers['Content-Type'] = 'application/json;charset=UTF-8'
        headers['Cookie'] = headers['Cookie'].split('kr_plus_project_id=')[0] + 'kr_plus_project_id=' + str(
            audio_data["project_id"])

        _data= {
            "user_id": 12186523,
            "title" : audio_data["title"],
            "column_id":"",
            "audio_values":audio.audio_values,
            "cover":audio.cover,
            "template_info":template_info(audio_data["title"],type=1),
            "publish_now": 1,
            "published_at": audio_data["published_at"]
        }

        re = self.request.put(url=_url, headers=headers, data=json.dumps(_data))
        print(re.text)
        print(audio_data)
        return audio_data

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


if __name__ == '__main__':
    i=I_audio()
    i.get_id("aaa")