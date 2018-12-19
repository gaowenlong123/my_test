from Api_Repository.Interface.CMS.article.I_article import I_article
import time

i = I_article()

def test():
    title = '测试第四范式,下线还展示文章'
    temp = []

    for m in range(1):
        data = i.get_ID(title)
        print(data)
        article_data = i.get_article_data(data=data)

        post_data = i.Cmod_article(article_data=article_data)

        i.publish(post_data)

        time.sleep(1)

        i.recommend(data['id'])

        temp.append(data['id'])


    print(temp)

def offline(alist):
    for id in alist:
        i.review(id)
        time.sleep(1)

def publish(alist):
    for id in alist:
        i.republish(id)


if __name__ == '__main__':
    pass