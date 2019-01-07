from Api_Repository.Interface.CMS.article.I_article import I_article
from Api_Repository.Data_Center.Entity import *
from Api_Repository.Interface.CMS.feed.I_feed import I_feed
from Api_Server.Decorate_Data.Extract_Dict_Value import *
from Api_Server.Decorate_Data.Extract_Value_Tostring import *
from Api_Server.Decorate_Data.Check_Response_Data import *


#0
# article = I_article()
feed = I_feed()


#1
# article_data=article.creat_publish("接口自动化测试")
# print(article_data)

#测试是否发布成功
# post_feed = feed.post_feed()
# post_feed=get_dict_value(post_feed ,template_path="data/data")
# re_list=keyValue_ToString_byIndex(post_feed ,by_index=[1],key_list=["id","title"])
# print(re_list)
# if article_data["id"] in re_list:  ???


#2
# article.recommend(article_data , recom_feed.tuijian)
#
# #测试是否推荐
# recom_list=feed.recom_feed()
# recom_list=get_dict_value(recom_list ,template_path="data/data")
# re_list=keyValue_ToString_byIndex(recom_list ,by_index=[1],key_list=["id","title"])
# print(re_list)
# if article_data["id"] in re_list:  ???



#3
# article.review(article_data)
#
# #测试是否下线
review_data=feed.post_ById({"id":10465059} )
review_data=get_dict_value(review_data ,template_path="data/data")
re_list=keyValue_ToString_byIndex(review_data ,by_index=[1],key_list=["id","state"])

# if "offline" in re_list:  ???



#4
# article.delete(article_data)
#
# #测试是否删除
dellect_data=feed.post_ById({"id":10462222259})
dellect_data=get_dict_value(dellect_data ,template_path="data/data")

if dellect_data ==[]:
    pass