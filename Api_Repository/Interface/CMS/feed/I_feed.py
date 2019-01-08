from Api_Server.Root.Interface import Interface
import os,requests,copy
from Api_Server.Support.Base_Enums import Enums
from Api_Repository.Data_Center.Entity import *
from Api_Server.Support.Base_Time import *
from Api_Repository.Data_Center.theme import *
from Api_Server.Support.Base_Compare import *

class I_feed(Interface):
    def __init__(self ,para=''):
        super(I_feed ,self).__init__()



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

    def post_feed(self ,state='',num=30):
        _url = self.url + '/post?state=published&per_page='+str(num)+'&page=1'
        rep = self.request.get(url=_url ,headers=self.Headers)
        return rep.json()

    def post_ByState(self ,state='offline',num=15):
        _url = self.url + '/post?state='+state+'&per_page='+str(num)+'&page=1'
        rep = self.request.get(url=_url ,headers=self.Headers)
        return rep.json()


    def post_ById(self ,data):
        _url= self.url+'/post?id='+str(data["id"])
        rep = self.request.get(url=_url, headers=self.Headers)
        return rep.json()

    def recom_feed(self,feed=feed_id.tj ,num=15):
        _url = self.url + '/feed-stream?state=published&feed_id='+feed+'&per_page=' + str(num) + '&page=1'
        rep = self.request.get(url=_url, headers=self.Headers)
        # print(rep.json())
        return rep.json()

    def recom_feed_Bystate(self,state = state.offline ,feed=feed_id.tj ,num=15):
        _url = self.url + '/feed-stream?state='+state+'&feed_id=' + feed + '&per_page=' + str(num) + '&page=1'
        rep = self.request.get(url=_url, headers=self.Headers)
        # print(rep.json())
        return rep.json()

    def recom_feed_ById(self ,id ,feed=feed_id.tj):
        _url = self.url + '/feed-stream?entity_id='+str(id)+'&feed_id='+feed
        rep = self.request.get(url=_url, headers=self.Headers)
        print(rep.json())
        return rep.json()

if __name__ == '__main__':
    pass
    i =I_feed()
    # i.post_feed()
    # i.recom_feed()
    i.recom_feed_ById(10465620)

