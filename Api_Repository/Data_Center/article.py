
def template_info(title ,template_type=0):
    '''
    :param title:     标题
    :param template_type:   0 = 小图 1 = 大图 2 = 多图
    :return:
    '''
    if template_type == 0:
        temp = "{\"template_type\":\"small_image\",\"template_title\":\""+title+"\",\"template_title_isSame\":true,\"template_cover\":[\"https://pic.36krcnd.com/201812/11045923/85a7hciqiu6rizft\"]}"
        pass
    elif template_type == 1:
        temp = "{\"template_type\":\"big_image\",\"template_title\":\""+title+"\",\"template_title_isSame\":true,\"template_cover\":[\"https://pic.36krcnd.com/201812/11064542/31mpasztx1uep8s5\"]}"
        pass
    elif template_type == 2:
        temp = "{\"template_type\":\"multi_image\",\"template_title\":\""+title+"\",\"template_title_isSame\":true,\"template_cover\":[\"https://pic.36krcnd.com/201812/11065244/lkkcikdrcuoai9k5\",\"https://pic.36krcnd.com/201812/11065251/xssz1apxcakog2jq\",\"https://pic.36krcnd.com/201812/11065302/sfubsvx52cz84zt9\"]}"
        pass
    else:
        print('输入的 template_type 错误')
        temp=''

    return temp

class content:
    dada="<p>哒哒</p>"
    pass

#web 的图片
class cover:
    web = "https://pic.36krcnd.com/201812/11051635/xqqqybmru90k2xfu"
    dog="https://pic.36krcnd.com/201812/20035532/oe1q5b1ak2q7jmp5"
    girl="https://pic.36krcnd.com/201812/20035835/pwp04kjx84ty0lot"
    city="https://pic.36krcnd.com/201812/20040504/aefrhr7cre5d4q82"
    pass

def ramdom_cover():
    import random
    index = random.randint(1, 4)
    if index == 1 :
        return cover.web
    elif index == 2:
        return cover.dog
    elif index ==3:
        return cover.city
    else:
        return cover.girl

class report_type:
    chuang= "创投观察"
    pass

class motifs:
    one=[]
    pass

class summary:
    sum = "文章摘要"


if __name__ == '__main__':
    import random
    print(random.randint(1,3))