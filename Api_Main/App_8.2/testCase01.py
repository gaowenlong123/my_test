from Api_Repository.Interface.CMS.article.I_article import I_article
from Api_Repository.Interface.CMS.feed_stream.I_feed_streem import I_feed_streem
from Api_Repository.Data_Center.Entity import *
from Api_Repository.Interface.CMS.feed.I_feed import I_feed
from Api_Server.Decorate_Data.Extract_Dict_Value import *
from Api_Server.Decorate_Data.Extract_Value_Tostring import *
from Api_Server.Asert.asert_property import *
from Api_Server.Asert.asert_equal import *
from Api_Repository.Interface.App.channel.channel_V8_2.I_channel_V8_2 import I_channel_V8_2
from Api_Server.Support.Base_APP import *
from Api_Repository.Interface_params_test.test import *

import unittest
class test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.article = I_article()
        cls.feed = I_feed()
        cls.feed_stream = I_feed_streem()
        cls.channel_recom = I_channel_V8_2(channel_type.recom)
        cls.result_dict = {}
        cls.test_result=[]


    def setUp(self):

        print("测试开始", "----" * 20)
        self.article_data = self.article.creat_publish("App_v8.2测试")
        # 测试是否发布成功
        post_feed = self.feed.post_feed()
        post_feed = get_dict_value(post_feed, template_path="data/data")
        asert_data1 = keyValue_ToString_byIndex(post_feed, by_index=[1], key_list=["id", "title"])
        # print(asert_data1)
        result1 = asert_property_ById(self.article_data, asert_data1, "title")
        # print(result1)
        self.result_dict.update({"发布文章": result1})



        self.article.recommend(self.article_data, recom_feed.tuijian)
        #
        # 测试是否推荐
        recom_list = self.feed.recom_feed()
        recom_list = get_dict_value(recom_list, template_path="data/data")
        self.recom_data = keyValue_ToString_byIndex(recom_list, by_index=[1], key_list=["id", "title"])
        # print(self.recom_data)
        result2 = asert_property(self.article_data, self.recom_data, "title")
        # print(result2)
        self.result_dict.update({"推荐文章": result2})



    def test1(self):
        '''
            推荐到频道信息流
        '''
        start = time_Stamp()
        while(True):
            _data = App_request()
            feed_data = get_dict_value(_data, template_path="data/itemList")
            asert_data = keyValue_ToString_byIndex(feed_data,by_index=[2], key_list=["itemType","widgetTitle","categoryTitle","route"])
            end = time_Stamp()
            if asert_data["data"][0].get("widgetTitle" ,None) == self.article_data["title"]:
                temp_str="测试成功，耗时"+str(end-start)+"秒"
                self.result_dict.update({"test1": temp_str})
                self.assertEqual(0, 0)
                break

            if end - start >120:
                temp_str = "测试失败，耗时" + str(end - start) + "秒"
                self.result_dict.update({"test1": temp_str})
                self.assertEqual(0,1,msg="测试失败，耗时" + str(end - start) + "秒")
                break
            time.sleep(2)


    # def test2(self):
    #     print('22')



    def tearDown(self):
        self.feed_stream.offline(self.recom_data["data"])
        # 在推荐频道下线
        _data1 = self.feed.recom_feed_ById(self.article_data)
        offline_data = get_dict_value(_data1, template_path="data/data")
        asert_data5 = keyValues_ToString(offline_data, key_list=["state"])
        result5 = asert_equal(asert_data5, "state", "offline")
        self.result_dict.update({"推荐频道下线文章": result5})



        # 在推荐频道删除   被删除，只是状态改变了
        self.feed_stream.delete(self.recom_data["data"])
        # 在推荐频道下线
        _data2 = self.feed.recom_feed_ById(self.article_data ,state='deleted')
        delete_data = get_dict_value(_data2, template_path="data/data")
        asert_data6 = keyValues_ToString(delete_data, key_list=["state"])
        result6 = asert_equal(asert_data6, "state", "deleted")
        self.result_dict.update({"推荐频道删除文章": result6})



        self.article.review(self.article_data)  # 操作
        # 测试是否下线
        review_data = self.feed.post_ById(self.article_data)  # 为了验证的请求
        review_data = get_dict_value(review_data, template_path="data/data")  # 做请求的校验，拿出有效值
        asert_data3 = keyValue_ToString_byIndex(review_data, by_index=[1], key_list=["id", "state"])  # 拿出具体值为了做进一步值的校验
        # asert_property({},asert_data ,"state" ,property_value="offine")
        result3 = asert_property_ById(self.article_data, asert_data3, "state", property_value="offline")
        # print(result3)
        self.result_dict.update({"下线文章": result3})


        self.article.delete(self.article_data)
        # #测试是否删除
        dellect_data = self.feed.post_ById(self.article_data)
        dellect_data = get_dict_value(dellect_data, template_path="data/data")
        # print(dellect_data)
        result4 = asert_equal(dellect_data, "data", targrt=[])
        # print(result4)
        self.result_dict.update({"删除文章": result4})



        print("测试结束", "****" * 20)
        for key in self.result_dict:
            try:
                if self.result_dict[key].get("result" ,None) !=None:
                    print(key + "==>" + str(self.result_dict[key]['result']))
                else:
                    #如果字典没有该字段
                    print(key + "==>" + str(self.result_dict[key]))
            except(AttributeError ):
                #如果是字符串，不是字典
                print(key + "==>" + str(self.result_dict[key]))
        self.result_dict.clear()


if __name__=='__main__':
    unittest.main()