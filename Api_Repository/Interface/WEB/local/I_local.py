# 地方站
import os , requests ,time
from Api_Server.Support.Base_Enums import Enums
from Api_Server.Root.Interface import Interface
from Api_Server.Support.Base_Compare import *
from Api_Repository.Data_Center.Entity import *
from Api_Repository.Interface.CMS.article.I_article import I_article

# class I_local(Interface):
    # def __init__(self,param = ''):
    #     super(I_local ,self).__init__()



class I_local():
    def __init__(self ,param=''):
        self.url = "http://test02.36kr.com/pp/api"
        self.request=requests.session()

    def new_post(self ,pp=pp_id.xian ,num=10):
        '''
        https://test02.36kr.com/pp/api/feed-stream?feed_id=316&project_id=96&per_page=20
        :param chanel:
        :return:
        '''
        _url = self.url + '/feed-stream?feed_id='+str(get_feed_id(pp))+'&project_id='+str(pp)+'&per_page=20&cc=yes'

        re= self.request.get(_url)
        temp = re.json()['data']['items'][:num]
        _list=[]

        for dict in temp:
            s1=map(dict,'title',"无")
            s2=map(dict , 'entity_type' ,"无")
            _list.append(s1+":"+s2)
        print("资讯==>",_list)
        return temp

    def head_banner(self,pp=pp_id.xian):
        '''
        https://test02.36kr.com/pp/api/focus?project_id=86&type=local_station_banner&cc=yes
        :param id:
        :return:
        '''
        _url = self.url + '/focus?project_id='+str(pp)+'&type=local_station_banner'
        _list=[]
        re = self.request.get(_url)
        temp = re.json()['data']['items']
        for dict in temp:
            _list.append(map(dict , 'title','无'))
        print("焦点图==>",_list)
        return temp

    def site_list(self):
        _url = self.url + '/local-station/sites'
        _list = []

        re = self.request.get(_url)
        temp = re.json()['data']

        for dict in temp:
            _list.append(map(dict, 'name', "无"))
            _list.append(map(dict, 'project_id', "无"))   #品牌ID可选
            _list.append(map(dict, 'web_feed_id', "无"))
        print(_list)
        return _list

    def flashs(self,pp=pp_id.xian):
        '''
        /pp/api/newsflash?project_id=1&    b_id=1 ???
        :param id:
        :return:
        '''
        _url = self.url + '/newsflash?project_id='+str(pp)
        _list = []
        re = self.request.get(_url)
        temp = re.json()['data']['items'][:10]

        for dict in temp:
            _list.append(map(dict, 'title', '无'))
        print("快讯==>",_list)
        return temp

    def web_fix_feedstream(self):
        '''
        http://test02.36kr.com/pp/api/focus?type=web_stream_pin
        :return:
        '''
        _url = self.url + '/focus?type=web_stream_pin'
        _list = []
        re = self.request.get(_url)
        temp = re.json()['data']['items']
        for dict in temp:
            _list.append(map(dict, 'title', '无'))
        print("焦点图==>", _list)
        return _list

    # 有问题
    def left_channel(self):
        _url = self.url + '/feed?type=web'
        _list = []

        re = self.request.get(_url)
        temp = re.json()['data']['items']

        for dict in temp:
            _list.append(map(dict, 'name', "无"))
        print(_list)
        return _list

    def recom_monographic(self, id):
        _url = self.url + '/focus?type=chosen_monographic&per_page=3'

        re = self.request.get(_url)
        temp = re.json()['data']['items'][:id]

        for i in temp:
            print(i)
            print('-' * 50)

        return temp

    def flash_ip(self,ip):
        '''
        http://test02.36kr.com/pp/api/newsflash?project_id=1&b_id=&per_page=20&client_ip=220.174.166.255
        :return:
        '''
        _url = self.url + '/newsflash?project_id=1&b_id=&per_page=20&client_ip=' + str(ip)
        _list = []
        re = self.request.get(_url)
        temp = re.json()['data']['items'][:30]
        print(_url)
        for dict in temp:
            s1=map(dict, 'project_id', '无')
            s2 = map(dict, 'station_info', '无')
            _list.append(str(s1)+': '+ str(s2))
        print("快讯==>", _list)


if __name__ == '__main__':
    i = I_local()
    # i.site_list()
    #
    #
    # i.head_banner()
    # i.flashs()
    # i.new_post(pp_id.huzhou)

    # while True:
    #     temp=i.web_fix_feedstream()
    #     print(temp[0])
    #     if "2" in temp[0]:
    #         from Api_Server.Support.Base_Time import *
    #         print(get_time())
    #         break
    #
    #     time.sleep(1)

    a=["124.116.239.242" ,"220.174.1.222" ,"120.40.134.160" ,"120.42.37.178" ,"218.72.111.75"]
    for m in a:
        i.flash_ip(m)






