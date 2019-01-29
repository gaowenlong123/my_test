import unittest
from Api_Server.Root_Gateway.Base_request import *
from Api_Server.Root_Gateway.Base_DateCenter import *
from Api_Server.Decorate_Data.Extract_Value_Tostring import *
from Api_Server.Decorate_Data.Extract_Dict_Value import *
from Api_Server.Asert.asert_http import *



class Top_feed(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        globals()["asert_data"] = {}
        cls.result_dict={}
        pass

    def setUp(self):
        print("测试开始", "****" * 20)

    def test1_homedaily(self):

        rep_data = App_request(daysign_feed(isFeed=False), environment=1)
        _data = get_dict_value(rep_data, template_path='data')
        globals()["asert_data"]=keyValues_ToString(data=_data , key_list=["id", "currentTimeFormat", "title", "route"])
        self.result_dict.update({"首页日签" : asert_http(rep_data) })
        time.sleep(1)

    def test2_dailyfeed(self):
        #全局变量
        asert_data = globals()["asert_data"]["data"]

        rep_data = App_request(daysign_feed(isFeed=True), environment=1)
        _data = get_dict_value(rep_data, template_path='data/dailywordList')
        target_data = keyValue_ToString_byIndex(data=_data, by_index=[1, 2, 3],
                                                key_list=["id", "effectTimeFormat", "widgetTitle", "route"])
        self.result_dict.update({"日签信息流": asert_http(rep_data)})


        #测试首个是否匹配
        queueValues_compareToString(asert_data , target_data["data"][0])

        if asert_data["id"] == target_data["data"][0]["id"] and asert_data["route"] == target_data["data"][0]["route"]:
            self.result_dict.update({"检查":"首页日签与信息流首位相等"})
        else:
            self.result_dict.update({"检查":"首页日签与信息流首位不相等相等" })
        time.sleep(1)


    def test3_topicFeed(self):

        rep_data = App_request(topic_data(isChosen=False), environment=1)
        _data = get_dict_value(rep_data, template_path='data/topicList')
        keyValue_ToString_byIndex(data=_data ,by_index=[1,2,3] ,key_list=["categoryId", "categoryTitle"])
        self.result_dict.update({"专题信息流" : asert_http(rep_data) })
        time.sleep(1)

    def test4_topicChosen(self):

        rep_data = App_request(topic_data(isChosen=True), environment=1)
        _data = get_dict_value(rep_data, template_path='data/topicList')
        keyValues_ToString(data=_data , key_list=["categoryId", "categoryTitle"])
        self.result_dict.update({"精选专题信息流" : asert_http(rep_data) })
        time.sleep(1)


    def tearDown(self):
        print("测试结束", "****" * 20)
        for key in self.result_dict:
            if self.result_dict[key] != True:
                print(key + "===========================>" + str(self.result_dict[key]))
            else:
                print(key + "==>" + str(self.result_dict[key]))

        self.result_dict.clear()
        input("输入任意值，点击继续")





if __name__=='__main__':
    unittest.main()