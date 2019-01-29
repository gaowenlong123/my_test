import unittest
from Api_Server.Root_Gateway.Base_request import *
from Api_Server.Root_Gateway.Base_DateCenter import *
from Api_Server.Decorate_Data.Extract_Value_Tostring import *
from Api_Server.Decorate_Data.Extract_Dict_Value import *
from Api_Server.Asert.asert_http import *

class search_feed(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_data = search_type.get_all()
        cls.result_dict={}
        pass

    def setUp(self):
        print("测试开始", "****" * 20)

    def test1_searchfeed(self):

        rep_data = App_request(search_data(), environment=1)
        article_data = get_dict_value(rep_data, template_path='data/article/itemList')
        newsflash_data = get_dict_value(rep_data, template_path='data/newsflash/itemList')
        audio_data = get_dict_value(rep_data, template_path='data/audio/itemList')
        author_data = get_dict_value(rep_data, template_path='data/author/itemList')
        video_data = get_dict_value(rep_data, template_path='data/video/itemList')
        theme_data = get_dict_value(rep_data, template_path='data/theme/itemList')
        topic_data = get_dict_value(rep_data, template_path='data/topic/itemList')

        keyValue_ToString_byIndex(data=article_data, by_index=[1],
                                      key_list=["itemId", "widgetTitle", "route"])
        keyValue_ToString_byIndex(data=newsflash_data, by_index=[1],
                                      key_list=["itemId", "widgetTitle", "route"])
        keyValue_ToString_byIndex(data=audio_data, by_index=[1],
                                      key_list=["itemId", "widgetTitle", "route"])
        keyValue_ToString_byIndex(data=video_data, by_index=[1],
                                      key_list=["itemId", "widgetTitle", "route"])
        keyValue_ToString_byIndex(data=theme_data, by_index=[1],
                                  key_list=["itemId", "widgetTitle", "route"])
        keyValue_ToString_byIndex(data=topic_data, by_index=[1],
                                  key_list=["itemId", "widgetTitle", "route"])
        keyValue_ToString_byIndex(data=author_data, by_index=[1],
                                      key_list=["authorId", "authorName", "route"])


        self.result_dict.update({"搜索信息流" : asert_http(rep_data) })
        time.sleep(1.5)


    def test2_searchByType(self):
        for value in self.all_data:
            print("-" * 20, "测试 %s 搜索" % value, "-" * 20)
            rep_data = App_request(search_ByType(value), environment=1)
            _data = get_dict_value(rep_data, template_path='data/itemList')
            keyValue_ToString_byIndex(data=_data, by_index=[1, 2, 3],
                                      key_list=["itemId", "widgetTitle", "authorName", "route"])
            self.result_dict.update({value+"搜索" : asert_http(rep_data) })
            time.sleep(1.5)

    def test3_searchNone(self):

        rep_data = App_request(search_data(isNone=True), environment=1)
        _data = get_dict_value(rep_data, template_path='data/recomArticleList')
        keyValue_ToString_byIndex(data=_data, by_index=[1, 2 ,3],
                                  key_list=["itemId", "widgetTitle", "route"])

        self.result_dict.update({"Null全量搜索": asert_http(rep_data)})
        time.sleep(1.5)

    def test4_searchTypeNone(self):
        for value in self.all_data:
            print("-" * 20, "测试 %s 搜索" % value, "-" * 20)
            rep_data = App_request(search_ByType( value ,isNone=True ), environment=1)
            _data = get_dict_value(rep_data, template_path='data/recomArticleList')
            keyValue_ToString_byIndex(data=_data, by_index=[1, 2, 3],
                                      key_list=["itemId", "widgetTitle", "route"])
            self.result_dict.update({value+" Null搜索" : asert_http(rep_data) })
            time.sleep(1.5)


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