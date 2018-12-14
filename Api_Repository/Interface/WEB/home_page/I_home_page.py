#首页信息流  ,不需要cookie
import requests

class I_home_page():
    def __init__(self):
        pass
        self.url = "http://test02.36kr.com/pp/api"
        self.request = requests.session()

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

        re = self.request.get(_url)
        temp = re.json()['data']['items']

        # for dict in temp:
        #
            # if key == 'name':
            #     print(i)
            #     print('-' * 50)

        return temp

    def recom_monographic(self, id):
        _url = self.url + '/aggregation-entity?type=web_latest_article&per_page=30'

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

    # i.new_post(2)
    # i.head_banner(1)
    # i.flashs(5)


    # i.left_channel()  ??

