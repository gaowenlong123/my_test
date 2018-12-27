import random
class cover:
    A="https://pic.36krcnd.com/201812/27113229/t9xq3sd64e43bg7t"
    human="https://pic.36krcnd.com/201812/27121429/vxkbh5v3hboqaq6h"

class web_cover:
    W="https://pic.36krcnd.com/201812/27113221/ylljcn8fo3wj9wwa"
    music="https://pic.36krcnd.com/201812/27121411/7otzprtekwwh7fpf"

class list:
    #展开模板
    list="{\"layout_data\":[{\"name\":\"板块名称\",\"type\":\"0\",\"childList\":[{\"type\":\"post\",\"list_type\":\"small\",\"name\":\"模块名称-文章\",\"ids\":\"10464600\"},{\"type\":\"newsflash\",\"name\":\"模块名称-快讯\",\"ids\":\"20995\"}]}]}"

def template_info(title ,type =0):
    if type == 0: # 小图
        return "{\"template_type\":\"small_image\",\"template_title\":\""+ title +"\",\"template_title_isSame\":true,\"template_cover\":[\"https://pic.36krcnd.com/201812/27113326/t0mzz7l103e0miwn\"],\"template_extra\":{\"entity_list\":[]}}"
    elif type == 1: # 大图
        return "{\"template_type\":\"big_image\",\"template_title\":\""+ title +"\",\"template_title_isSame\":true,\"template_cover\":[\"https://pic.36krcnd.com/201812/27113326/t0mzz7l103e0miwn\"],\"template_extra\":{\"entity_list\":[]}}"
    else:        #  展开模板
        return "{\"template_type\":\"unfold_text\",\"template_title\":\""+ title +"\",\"template_title_isSame\":true,\"template_cover\":[\"https://pic.36krcnd.com/201812/27113326/t0mzz7l103e0miwn\"],\"template_extra\":{\"entity_list\":[{\"column_id\":null,\"column_name\":null,\"id\":10464600,\"title\":\"展开模板-文章\",\"type\":\"post\"},{\"column_id\":null,\"column_name\":null,\"id\":20995,\"title\":\"展开模板-快讯\",\"type\":\"newsflash\"},{\"column_id\":null,\"column_name\":null,\"id\":2404,\"title\":\"展开模板-视频\",\"type\":\"video\"}]}}"
