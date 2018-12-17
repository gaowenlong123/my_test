# 地方站
import os , requests
from Api_Server.Support.Base_Enums import Enums
from Api_Server.Root.Interface import Interface

# class I_local(Interface):
    # def __init__(self,param = ''):
    #     super(I_local ,self).__init__()


class I_local():
    def __init__(self):
        self.url = "http://test02.36kr.com/pp/api"
        self.request=requests.session()

    def  new_post(self , id):
        _url = self.url + '/aggregation-entity?type=web_latest_article&per_page=30'

        re= self.request.get(_url)
        temp = re.json()['data']['items'][:id]

        for i in temp:
            print(i)
            print('-'*50)
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
    i = I_local()
#







