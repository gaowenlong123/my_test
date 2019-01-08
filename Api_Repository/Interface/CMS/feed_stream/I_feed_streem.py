from Api_Server.Root.Interface import Interface
from Api_Server.Support.Base_Time import *
from Api_Repository.Data_Center.newsflash import *
from Api_Server.Support.Base_Enums import Enums
import copy , requests ,os ,json
from Api_Repository.Data_Center.audio import *
from Api_Repository.Data_Center.Entity import *

class I_feed_streem(Interface):
    def __init__(self ,param = ''):
        super(I_feed_streem ,self).__init__()
        pass



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
        self.url='http://cmstest02.36kr.com/api/feed-stream'

        self.request = requests.session()


    def delete(self,data):
        '''
        可以共用
        :param data:
        :return:
        '''
        _url = self.url+'/'+str(data["id"])
        headers = copy.deepcopy(self.Headers)
        headers['Content-Type'] = 'application/json;charset=UTF-8'
        headers['Cookie'] = headers['Cookie'].split('kr_plus_project_id=')[0] + 'kr_plus_project_id=' + str(
            data["project_id"])

        re = self.request.delete(url=_url, data={}, headers=headers)
        print(re.text)

    def offline(self,data):
        '''
        可以共用
        :param data:   id 是这个信息流的id ，不是 文章实体接口的id  ！！！
        :return:
        '''
        _url = self.url+'/'+str(data["id"])+'/offline'
        headers = copy.deepcopy(self.Headers)
        headers['Content-Type'] = 'application/json;charset=UTF-8'
        headers['Cookie'] = headers['Cookie'].split('kr_plus_project_id=')[0] + 'kr_plus_project_id=' + str(
            data["project_id"])

        re = self.request.put(url=_url, data={}, headers=headers)
        print(re.text)

if __name__ == '__main__':
    i = I_feed_streem()
    # i.offline({"id":63702, "project_id":1})
    # i.delete({"id":63702 , "project_id":1})      只是状态为deleted


