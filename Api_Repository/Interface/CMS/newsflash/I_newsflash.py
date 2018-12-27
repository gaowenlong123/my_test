from Api_Server.Root.Interface import Interface
from Api_Server.Support.Base_Time import *
from Api_Repository.Data_Center.newsflash import *
from Api_Server.Support.Base_Enums import Enums
import copy , requests ,os
from Api_Repository.Data_Center.Entity import *

class I_newsflash(Interface):
    def __init__(self ,param = ''):
        super(I_newsflash ,self).__init__()





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

        # 结构不复杂 (无图无链接)
        self.post_data = {"title": "???",
                           "catch_title": "",
                           "select": False,
                           "cover": "",
                           "description": "???",
                           "news_url_type": "",
                           "column_id": "???",
                           "extraction_tags": "[]",
                           "is_top": 0,
                           "pin": 0,
                           "template_info": "??",
                           "project_id": "1"}

        # 有图有链接
        self._data = {"title": "新建测试快讯推送",
                      "catch_title": "",
                      "select": True,
                      "cover": "https://pic.36krcnd.com/201812/13041220/ecbfboc94791rg96.jpeg",
                      "description": "内容",
                      "news_url_type": "product_url",
                      "column_id": "72",
                      "extraction_tags": "[]",
                      "is_top": 0,
                      "pin": 0,
                      "news_url": "https://www.baidu.com",
                      "template_info": "{\"template_type\":\"no_image\",\"template_title\":\"新建测试快讯推送\",\"template_cover\":[]}",
                      "project_id": "1"}



    def publish(self ,title ,project_id=1 ):
        '''
        :param title:  快讯标题
        :return:  快讯ID 标题
        '''
        _url = 'http://cmstest02.36kr.com/api/newsflash'
        headers = copy.deepcopy(self.Headers)
        flash_data = copy.deepcopy(self.post_data)
        headers['Content-Type'] = 'application/json;charset=UTF-8'
        headers['Cookie'] = headers['Cookie'].split('kr_plus_project_id=')[0] + 'kr_plus_project_id=' + str(project_id)

        #个性化数据
        flash_data["title"]=get_name(project_id) + title + get_time()
        flash_data["description"] = description.wu
        flash_data["column_id"] = column_id.qita
        flash_data["template_info"] = template_info(flash_data["title"])

        # print(flash_data)
        re =self.request.post(url=_url ,headers=headers ,data=flash_data)
        print(re.text)

        #返回值
        try:
            re_dict= {
                'id':re.json()["data"]["id"],
                'title':flash_data["title"],
                'project_id':project_id
            }
        except:
            re_dict={}
        return re_dict

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

        _url = self._url + '/newsflash/' + str(data["id"]) + '/recommend'
        headers = copy.deepcopy(self.Headers)
        headers['Content-Type'] = 'application/json;charset=UTF-8'
        headers['Cookie'] = headers['Cookie'].split('kr_plus_project_id=')[0] + 'kr_plus_project_id=' + str(
            data["project_id"])
        _data = {"recommend_info": feed}

        re = self.request.put(url=_url, headers=headers, data=_data)
        print(re.text)


    def review(self,data):
        '''
        http://cmstest02.36kr.com/api/newsflash/21308/review
        :param data: {'id': 10465323, 'open_at': 1545284393763, 'project_id': 86}
        :return:
        '''
        _url = self._url + '/newsflash/'+str(data["id"])+'/review'
        headers = copy.deepcopy(self.Headers)
        headers['Content-Type'] = 'application/json;charset=UTF-8'
        headers['Cookie'] = headers['Cookie'].split('kr_plus_project_id=')[0] + 'kr_plus_project_id=' + str(
            data["project_id"])

        re=self.request.put(url=_url ,headers=headers,data={})
        print(re.text)


    def republish(self ,data):
        '''
        :param id:
        :return:{"code":0}
        '''
        _url = self._url + '/newsflash/' + str(data["id"])+'/publish'
        headers = copy.deepcopy(self.Headers)
        headers['Content-Type'] = 'application/json;charset=UTF-8'
        headers['Cookie'] = headers['Cookie'].split('kr_plus_project_id=')[0] + 'kr_plus_project_id=' + str(
            data["project_id"])

        re = self.request.put(url=_url, headers=headers, data={})
        print(re.text)



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
    i = I_newsflash()
    data=i.publish('测试地方站快讯  ' ,project_id=pp_id.xiamen)
    # i.push(data)



