#
from Api_Repository.Data_Center.focus import *
from Api_Server.Root.Interface import Interface
from Api_Server.Support.Base_Time import *
from Api_Repository.Data_Center.newsflash import *
from Api_Server.Support.Base_Enums import Enums
import copy , requests ,os


class I_focus(Interface):
    '''
    Cms 焦点图
    '''
    def __init__(self ,param = ''):
        super(I_focus ,self).__init__()

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
        # 显示标题 ，外链
        self.post_data = {"url":"",
                          "hidden_title":"0",
                          "title":"",
                          "cover":"", #三金
                          "start_time":None,
                          "end_time":None,
                          "type":"feed",
                          "feed_id":"",
                          "entity_type":""
                          }

        self.url = 'https://cmstest02.36kr.com/api/focus'



    def publish(self  ,feed ,cover ,type=0 ):
        '''
        :param type:  0 外链  1 专辑  2 专栏
        :param  feed : 信息流
        :return:  焦点图ID 标题
        '''
        headers = copy.deepcopy(self.Headers)
        _data = copy.deepcopy(self.post_data)
        headers['Content-Type'] = 'application/json;charset=UTF-8'

        #个性化数据
        temp = get_info(type)
        _data["title"]=temp["title"]
        _data["url"] = temp["url"]
        _data["entity_type"] = temp["entity_type"]
        _data["cover"] = cover
        _data["feed_id"] = feed

        # print(flash_data)
        re =self.request.post(url=self.url ,headers=headers ,data=_data)
        print(re.text)

        #返回值
        re_dict= {
            'id':re.json()["data"]["id"],
            'title':_data["title"]
        }
        return re_dict



# 方法会抽出去
    def push(self , data):
        '''
        :param data: 包含ID 数据
        :return:
        '''
        _url = 'http://cmstest02.36kr.com/api/push'
        headers = copy.deepcopy(self.Headers)
        headers['Content-Type'] = 'application/json;charset=UTF-8'

        ar_post_data = {"sound": "1",
                        "title": data['title'],
                        "content": "推送",
                        "entity_type": "newsflash",
                        "entity_id": data['id'],
                        "publish_now": 1,
                        "published_at": "",
                        "expire_time": "4"}

        re = self.request.post(url=_url, headers=self.Headers, data=ar_post_data)
        print(re.text)




if __name__ == '__main__':
    i = I_focus()
    i.publish(feed.bzsj , cover.sanjin, type=0 )