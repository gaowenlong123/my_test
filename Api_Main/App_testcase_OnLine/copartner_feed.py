import unittest
from Api_Server.Root_Gateway.Base_request import *
from Api_Server.Root_Gateway.Base_DateCenter import *
from Api_Server.Decorate_Data.Extract_Value_Tostring import *
from Api_Server.Decorate_Data.Extract_Dict_Value import *
from Api_Server.Asert.asert_http import *

class corpartner_feed(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result_dict={}
        pass

    def setUp(self):
        print("测试开始", "****" * 20)

    def test_feed(self):

        rep_data = App_request(copartner_data(), environment=1)
        _data = get_dict_value(rep_data, template_path='data/feedList')
        keyValue_ToString_byIndex(data=_data, by_index=[1, 2, 3 ],
                                      key_list=["feedId", "userName", "userSummary", "route"])

        self.result_dict.update({"创投圈信息流" : asert_http(rep_data) })
        time.sleep(1.5)



    #万一之后需要焦点图了
    # def test_focus(self):
    #
    #     rep_data = App_request(discovery_focus(), environment=1)
    #     _data = get_dict_value(rep_data, template_path='data/bannerList')
    #     keyValue_ToString_byIndex(data=_data, by_index=[1, 2],
    #                                   key_list=["itemType", "widgetTitle", "categoryTitle", "route"])
    #
    #     self.result_dict.update({"发现页焦点图" : asert_http(rep_data) })
    #     time.sleep(1.5)



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