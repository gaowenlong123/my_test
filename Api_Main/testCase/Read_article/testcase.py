from Api_Repository.Interface.CMS.article.I_article import I_article
from Api_Repository.Interface.CMS.feed_stream.I_feed_streem import I_feed_streem
from Api_Repository.Data_Center.Entity import *
from Api_Repository.Interface.CMS.feed.I_feed import I_feed
from Api_Server.Decorate_Data.Extract_Dict_Value import *
from Api_Server.Decorate_Data.Extract_Value_Tostring import *
from Api_Server.Asert.asert_property import *
from Api_Server.Asert.asert_equal import *

#字典的值是   列表还是字典需要注意，要先判断
# 基类方法一定要避免  数据格式不对，造成在方法里面的兼容

#0
article = I_article()
feed = I_feed()
feed_stream = I_feed_streem()
result_dict={}


print("测试开始" ,"----"*20)

#1
article_data=article.creat_publish("接口自动化测试123")
#测试是否发布成功
post_feed = feed.post_feed()
post_feed=get_dict_value(post_feed ,template_path="data/data")
asert_data1=keyValue_ToString_byIndex(post_feed ,by_index=[1],key_list=["id","title"])
# print(asert_data1)
result1=asert_property_ById(article_data ,asert_data1 ,"title")
# print(result1)
result_dict.update({"发布文章" :result1})



#2
article.recommend(article_data , recom_feed.tuijian)
#
#测试是否推荐
recom_list=feed.recom_feed()
recom_list=get_dict_value(recom_list ,template_path="data/data")
recom_data=keyValue_ToString_byIndex(recom_list ,by_index=[1],key_list=["id","title"])
# print(recom_data)
result2=asert_property(article_data ,recom_data ,"title")
# print(result2)
result_dict.update({"推荐文章" :result2})



#
feed_stream.offline(recom_data["data"])
#在推荐频道下线
_data1=feed.recom_feed_ById(article_data )
offline_data=get_dict_value(_data1 ,template_path="data/data")
asert_data5=keyValues_ToString(offline_data ,key_list=["state"])
result5=asert_equal(asert_data5 ,"state","offline" )
print(result5)
result_dict.update({"推荐频道下线文章" :result5})



#在推荐频道删除   被删除，只是状态改变了
feed_stream.delete(recom_data["data"])
#在推荐频道下线
_data2=feed.recom_feed_ById(article_data )
delete_data=get_dict_value(_data2 ,template_path="data/data")
asert_data6=keyValues_ToString(delete_data ,key_list=["state"])
# print(asert_data6)
result6=asert_equal(asert_data6 ,"state","deleted" )
# print(result6)
result_dict.update({"推荐频道删除文章" :result6})



#3
article.review(article_data)                                              #操作

#测试是否下线
review_data=feed.post_ById(article_data )                                   #为了验证的请求
review_data=get_dict_value(review_data ,template_path="data/data")         #做请求的校验，拿出有效值
asert_data3 = keyValue_ToString_byIndex(review_data ,by_index=[1],key_list=["id","state"])  #拿出具体值为了做进一步值的校验
# asert_property({},asert_data ,"state" ,property_value="offine")
result3=asert_property_ById(article_data,asert_data3 ,"state" ,property_value="offline")
# print(result3)
result_dict.update({"下线文章" :result3})



# #4
article.delete(article_data)

# #测试是否删除
dellect_data=feed.post_ById(article_data)
dellect_data=get_dict_value(dellect_data ,template_path="data/data")
# print(dellect_data)
result4=asert_equal(dellect_data ,"data" ,targrt=[])
# print(result4)
result_dict.update({"删除文章" :result4})



print("测试结束" ,"****"*20)
for i in result_dict:
    print(i + "==>" + str(result_dict[i]['result']))