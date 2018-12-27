#根据不同地方发布文章
from Api_Repository.Interface.CMS.article.I_article import I_article
from Api_Repository.Interface.CMS.newsflash.I_newsflash import I_newsflash
from Api_Repository.Data_Center.Entity import *
from Api_Repository.Interface.CMS.focus.I_focus import I_focus
from Api_Repository.Interface.CMS.theme.I_theme import I_theme
from Api_Repository.Interface.CMS.video.I_video import I_video
import time ,random


def create_article(i,title , project):


    data = i.get_ID(title, project)

    article_data = i.get_article_data(data=data)

    post_data = i.Cmod_article(article_data=article_data, data=data)

    i.publish(post_data, data=data)

    time.sleep(1)

    i.recommend(data)

    return data

def delete(i,data):

    i.review(data)
    time.sleep(1)
    i.delete(data)




def test_one(num ,title , project=1):
    i = I_article()
    temp_list = []
    for m in range(num):
        temp_list.append(create_article(i,title , project))

    print(temp_list)

    # input('是否删除文章')
    #
    # for list in temp_list:
    #     delete(i,data=list)
    #     time.sleep(1)

def test_two(title ,project):
    news = I_newsflash()
    data = news.publish(title ,project_id=project)

    time.sleep(1)
    news.recommend(data)

    # input("是否删除")
    #
    # news.review(data)

def test_focus(project ,nums=1):
    i = I_focus()

    ran=random.randint(0,2)
    for m in range(nums):
        i.publish(project_id=project, type=ran)

def test_theme(title ,project_id = 1):
    i = I_theme()
    data=i.publish(title=title ,project_id=project_id)

    time.sleep(1)
    i.recommend(data=data)

def test_video(title ,project_id=1):
    i = I_video()
    # data=i.get_Id(title ,pulish_time=2)
    data=i.get_Id(title ,project_id=project_id)
    i.Cmod_video(data)
    i.publish(data)

    time.sleep(1)
    i.recommend(data=data)

if __name__ == '__main__':
    pass

    # test_one(1,"测试定时发布文章" ,pp_id.zhuzhan)
    #地方站文章
    # test_one(1,"测试西安文章" ,pp_id.xian)
    # test_one(1, "测试海南文章", pp_id.hainan)
    # test_one(1, "测试福州文章", pp_id.fuzhou)
    # test_one(1, "测试湖州文章", pp_id.huzhou)  NO
    # test_one(1, "测试厦门文章", pp_id.xiamen)
    # test_one(2,'测试南京', pp_id.nanjing)
    # test_one(2,'测试成都', pp_id.chengdu)
    # test_one(2,'测试昆明', pp_id.kunming)
    # test_one(2,'测试青岛' ,pp_id.qingdao)


    # #地方站快讯
    # # test_two("主站",pp_id.zhuzhan)
    # test_two('测试西安快讯', pp_id.xian)
    # test_two('测试海南快讯', pp_id.hainan)
    # test_two('测试福州快讯', pp_id.fuzhou)
    # test_two('测试湖州快讯', pp_id.huzhou)NO
    # test_two('测试厦门快讯' ,pp_id.xiamen)
    # test_two('测试南京快讯', pp_id.nanjing)
    # test_two('测试成都快讯', pp_id.chengdu)
    # test_two('测试昆明快讯', pp_id.kunming)
    # test_two('测试青岛快讯' ,pp_id.qingdao)



    #测试地方站焦点图
    # test_focus(pp_id.xiamen,1)

    #话题
    # test_theme("测试西安话题" ,pp_id.xian)
    # test_theme('测试海南', pp_id.hainan)
    # test_theme('测试福州', pp_id.fuzhou)
    # test_theme('测试厦门' ,pp_id.xiamen)
    # test_theme('测试南京', pp_id.nanjing)
    # test_theme('测试成都', pp_id.chengdu)
    # test_theme('测试昆明', pp_id.kunming)
    # test_theme('测试青岛' ,pp_id.qingdao)


    #测试地方站视频
    # test_video("测试西安视v频" , pp_id.qingdao)
    # test_video('测试海南V', pp_id.hainan)
    # test_video('测试福州V', pp_id.fuzhou)
    test_video('测试厦门V', pp_id.xiamen)
    test_video('测试南京V', pp_id.nanjing)
    test_video('测试成都V', pp_id.chengdu)
    test_video('测试昆明V', pp_id.kunming)
    test_video('测试青岛V', pp_id.qingdao)