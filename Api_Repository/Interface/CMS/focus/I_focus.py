#
from Api_Repository.Data_Center.focus import *
from Api_Repository.Data_Center.Entity import *
from Api_Server.Root.Interface import Interface
from Api_Server.Support.Base_Time import *
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



    def publish(self  ,feed =0,project_id=1,type=0 ):
        '''
        新建到app的主站 或地方站
         # i.publish(feed=feed_id.bzsj ,type=0)  #主站推挤频道
        i.publish(project_id=pp_id.huzhou, type=0 )    #地方站

        :param type:  0 外链  1 专辑  2 专栏
        :param  feed : 信息流
        :project_ip  : 主站 还是地方站
        :return:  焦点图ID 标题
        '''
        headers = copy.deepcopy(self.Headers)
        _data = copy.deepcopy(self.post_data)
        headers['Content-Type'] = 'application/json;charset=UTF-8'

        if project_id !=1:
            headers['Cookie'] = headers['Cookie'].split('kr_plus_project_id=')[0] + 'kr_plus_project_id=' + str(project_id)
            feed =get_feed_id(project_id)
            temp = get_info(type ,get_name(project_id))
        else:
            temp = get_info(type,"")

        #个性化数据
        _data["title"]=temp["title"]
        _data["url"] = temp["url"]
        _data["entity_type"] = temp["entity_type"]
        _data["cover"] = get_cover(type)
        _data["feed_id"] = feed

        # print(flash_data)
        re =self.request.post(url=self.url ,headers=headers ,data=_data)
        print(re.text)

        #返回值
        re_dict= {
            'id':re.json()["data"]["id"],
            'title':_data["title"],
            'project_id':project_id
        }
        return re_dict


    def local_publish(self ,project_id):
        '''
        web端地方站焦点图
        :return:
        '''
        headers = copy.deepcopy(self.Headers)
        _data = copy.deepcopy(self.post_data)
        headers['Content-Type'] = 'application/json;charset=UTF-8'

        headers['Cookie'] = headers['Cookie'].split('kr_plus_project_id=')[0] + 'kr_plus_project_id=' + str(
                project_id)
        feed = get_feed_id(project_id)
        temp = get_info(0, get_name(project_id))


        # 个性化数据
        _data["title"] = temp["title"]
        _data["url"] = temp["url"]
        _data["type"] = "local_station_banner"
        _data["cover"] = get_cover(type)
        _data["feed_id"] = feed

        # print(flash_data)
        re = self.request.post(url=self.url, headers=headers, data=_data)
        print(re.text)

        # 返回值
        re_dict = {
            'id': re.json()["data"]["id"],
            'title': _data["title"],
            'project_id': project_id
        }
        return re_dict

    def review(self,data):
        '''
        可以共用
        http://cmstest02.36kr.com/api/focus/1032/review
        :param data:
        :return:
        '''
        _url = self.url+'/'+str(data["id"])+'/review'
        headers = copy.deepcopy(self.Headers)
        headers['Content-Type'] = 'application/json;charset=UTF-8'
        headers['Cookie'] = headers['Cookie'].split('kr_plus_project_id=')[0] + 'kr_plus_project_id=' + str(
            data["project_id"])

        re = self.request.put(url=_url, headers=headers)
        print(re.text)


    def get_data(self , id=357 ,type="published"):
        '''
        # 得到信息流的数据   只能得到App端的把
        http://cmstest02.36kr.com/api/focus?feed_id=357&state=drafted-published&type=feed&per_page=30&page=1
        :param id: 频道ID
        :type    offline 下线 ,  drafted  待发布
        :return:
        '''
        _url = self.url+'?feed_id='+str(id)+'&state='+type+'&type=feed&per_page=30&page=1'
        headers = copy.deepcopy(self.Headers)
        headers['Content-Type'] = 'application/json;charset=UTF-8'

        re = self.request.get(url=_url, headers=self.Headers)

        print(re.json()['data']['total'])
        re_list = re.json()['data']['data']

        return re_list




if __name__ == '__main__':
    i = I_focus()
    #需要解决跨品牌的问题
    # i.publish(feed=feed_id.bzsj ,type=0)  #app 主站推挤频道
    # i.publish(project_id=pp_id.huzhou, type=0 )    #app地方站


    # i.local_publish(pp_id.xian)          #发布web加点图

    # i.review({"id":1025 , "project_id":1})   #下线焦点图


    # i.get_data(id=314)


