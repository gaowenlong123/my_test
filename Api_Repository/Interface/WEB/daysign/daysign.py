import requests ,json
from Api_Server.Support.Base_Compare import *

class daysign():
    def __init__(self):
        self.url='http://gatewaytest36.36kr.com/api'
        self.request =requests.session()

    def home_daysign(self):
        _url=self.url+"/mis/dailyword"

        data = {
            "partner_id": "web",
            "param": {"siteId": 1, "platformId": 1}
        }
        headers = {
            'Content-Type': 'application/json;charset=UTF-8'
        }
        re = self.request.post(url='http://gatewaytest36.36kr.com/api/mis/dailyword', headers=headers,
                           data=json.dumps(data))

        try:
            _temp = re.json()["data"]
            # print(_temp)
            # for dict in _temp:

            print("time ===>" , map(_temp ,"currentTimeFormat" ,"无"))
            print(map(_temp ,'title' ,"无"))
            print(map(_temp ,"content" ,"无"))

        except:
            _temp={}

    def home_daysign1(self):
        _url = self.url + "/mis/dailyword/list"

        data = {
            # "partner_id": "web",
            "param": {"siteId": 1, "platformId": 1},
            "pageSize":20,
            "pageEvent":1,
        }
        headers = {
            'Content-Type': 'application/json;charset=UTF-8'
        }
        re = self.request.post(url='http://gatewaytest36.36kr.com/api/mis/dailyword', headers=headers,
                               data=json.dumps(data))
        print(re.text)
        try:
            _temp = re.json()["data"]

            # for dict in _temp:

            # print("time ===>", map(_temp, "currentTimeFormat", "无"))
            # print(map(_temp, 'title', "无"))
            # print(map(_temp, "content", "无"))

        except:
            _temp = {}


if __name__ == '__main__':
    i =daysign()
    i.home_daysign()
    i.home_daysign1()