#首页信息流  ,不需要cookie
from Api_Server.Support.Base_Compare import *
import requests

class I_home_page():
    def __init__(self):
        pass
        self.url = "http://test02.36kr.com/pp/api"
        self.request = requests.session()

    def new_post(self , id):
        _url = self.url + '/aggregation-entity?type=web_latest_article&per_page=30'
        _list=[]
        re= self.request.get(_url)
        temp = re.json()['data']['items'][:id]

        for dict in temp:
            s1 = map(dict, 'title', "无")
            s2 = map(dict, 'entity_type', "无")
            _list.append(s1 + ":" + s2)
        print("资讯==>", _list)
        return temp

    def head_banner(self, id):
        _url = self.url + '/focus?type=head_line_new&per_page=6'

        re = self.request.get(_url)
        temp = re.json()['data']['items'][:id]

        for i in temp:
            print(i)
            print('-' * 50)
        return temp

    def left_channel(self):
        _url = self.url + '/feed?type=web'
        _list=[]

        re = self.request.get(_url)
        temp = re.json()['data']['items']

        for dict in temp:
            _list.append(map(dict , 'name' , "无"))
        print(_list)
        return _list

    #有问题
    def recom_monographic(self, id):
        _url = self.url + '/focus?type=chosen_monographic&per_page=3'

        re = self.request.get(_url)
        temp = re.json()['data']['items'][:id]

        for i in temp:
            print(i)
            print('-' * 50)

        return temp

    def flashs(self, id):
        _url = self.url + '/newsflash'

        re = self.request.get(_url)
        temp = re.json()['data']['items'][:id]

        for i in temp:
            print(i)
            print('-' * 50)
        return temp

if __name__ == '__main__':
    i = I_home_page()

    i.new_post(16)
    # i.head_banner(1)
    # i.flashs(5)
    # i.left_channel()

    # i.recom_monographic(2)
