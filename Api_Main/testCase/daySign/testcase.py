from Api_Repository.Interface.MRS.DaySign.I_DaySign import I_DaySign
from Api_Repository.Interface.CMS.article.I_article import I_article


def test_ID():
    article = I_article()
    data=article.creat_publish("测试待发布文章" ,publish=0)
    article.review(data)


    day =I_DaySign()
    day.test_ID(data["id"])




if __name__ == '__main__':
    test_ID()