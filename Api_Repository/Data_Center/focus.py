# 链接隐藏标题
_data = {"url":"https://www.baidu.com",
                      "hidden_title":"1",
                      "title":"",
                      "cover":"https://pic.36krcnd.com/201812/14092046/qdsambm2lwea6hrz", #山
                      }


class url:
    baidu = "https://www.baidu.com"
    album_gohome =  "67"
    column_guigu = "238"



class title:
    pass

def get_info(type ,project):
    if type==0:
        return {'url': "https://www.baidu.com", 'title': project+"外链焦点图", "entity_type": ""}
    elif type==1:
        return {'url':"67" , 'title':"回家路上","entity_type":"album"}
    elif type==2:
        return {'url':"238" , 'title':"硅谷早知道" ,"entity_type":"column"}
    else:
        return {}

class cover:
    sanjin="https://pic.36krcnd.com/201812/14091412/8i9y3wysmfj1o4uh"
    village="https://pic.36krcnd.com/201812/14092046/qdsambm2lwea6hrz"
    music1="https://pic.36krcnd.com/201812/14092438/0cp6ab1o0kbqg5g7"
    music2="https://pic.36krcnd.com/201812/14092731/1gkii4bu7x25q3u4"


def get_cover(type):
    if type == 0 :
        return cover.village
    elif type ==1 :
        return cover.music1
    else:
        return cover.music2   #专栏



#信息流固定位
def feed_stream_fix(type ,position,feed):
    if position == 14:
        return {"extra":"{\"position\":14}",
                "entity_type":"general_post",
                "url":"http://www-test01.36kr.com/p/10465068",
                "type":type,
                "feed_id": feed,
                "hidden_title":"0"}
    else:
        return {}
