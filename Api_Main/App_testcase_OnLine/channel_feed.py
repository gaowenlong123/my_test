import unittest
from Api_Server.Root_Gateway.Base_request import *
from Api_Server.Root_Gateway.Base_DateCenter import *
from Api_Server.Support.Base_APP import *
from Api_Server.Decorate_Data.Extract_Value_Tostring import *
from Api_Server.Decorate_Data.Extract_Dict_Value import *
from Api_Server.Asert.asert_http import *

class channel_feed(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_data = channel_param.get_all()
        cls.result_dict={}
        pass

    def setUp(self):
        print("测试开始", "****" * 20)

    def test_feed(self):
        for key in self.all_data:
            print("-"*20,"测试 %s 频道"%key,"-"*20)
            rep_data = App_request(channel_data(self.all_data[key]), environment=1)
            _data = get_dict_value(rep_data, template_path='data/itemList')
            # keyValues_ToString(data=data2, key_list=["itemType","widgetTitle","categoryTitle","route"])
            keyValue_ToString_byIndex(data=_data, by_index=[1, 2, 3 ,7],
                                      key_list=["itemType", "widgetTitle", "categoryTitle", "route"])

            self.result_dict.update({key : asert_http(rep_data) })
            time.sleep(1.5)
            # input("请按任意键")

    def test_focus(self):
        for key in self.all_data:
            print("-"*20,"测试 %s 焦点图"%key,"-"*20)
            rep_data = App_request(focus_data(self.all_data[key]), environment=1)
            _data = get_dict_value(rep_data, template_path='data/bannerList')
            # keyValues_ToString(data=data2, key_list=["itemType","widgetTitle","categoryTitle","route"])
            keyValue_ToString_byIndex(data=_data, by_index=[1, 2],
                                      key_list=["itemType", "widgetTitle", "categoryTitle", "route"])

            self.result_dict.update({key : asert_http(rep_data) })
            time.sleep(1.5)
            # input("请按任意键")


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
