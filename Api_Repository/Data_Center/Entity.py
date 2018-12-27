class feed_id:
    tj="59"
    bzsj="357"

    web_new="331"

    hainan="314"
    xian="298"
    nanjing="300"
    chengdu="301"
    kunming="302"
    xiamen="317"
    fuzhou="318"
    huzhou="316"
    qingdao="315"
class pp_id:
    zhuzhan=1
    xian = 86
    nanjing = 87
    chengdu = 88
    kunming = 89
    hainan=90
    qingdao=92
    xiamen=95
    guiyang=93
    fuzhou=94
    huzhou=96
    guangzhou=97
    nanning=98

class recom_feed:
    tuijian="{\"feed_ids\":[59]}"

    #地方站
    xianan = "{\"feed_ids\":[298]}"
    nanjing="{\"feed_ids\":[300]}"
    chengdu="{\"feed_ids\":[301]}"
    kunming="{\"feed_ids\":[302]}"
    guangzhou="{\"feed_ids\":[321]}"
    hainan = "{\"feed_ids\":[314]}"
    qingdao="{\"feed_ids\":[315]}"
    xiamen = "{\"feed_ids\":[317]}"
    fuzhou = "{\"feed_ids\":[318]}"
    guiyang="{\"feed_ids\":[319]}"
    huzhou = "{\"feed_ids\":[316]}"
    nanning="{\"feed_ids\":[322]}"


a=['西安', 86, 298, '南京', 87, 300, '成都', 88, 301, '昆明', 89, 302, '广州', 97, 321, '福州', 94, 318, '南宁', 98, 322, '贵阳', 93, 319, '厦门', 95, 317, '湖州', 96, 316, '青岛', 92, 315, '海南', 90, 314]

def local_recom_feed(project):
    if project == pp_id.xian:
        return recom_feed.xianan
    elif project == pp_id.hainan:
        return recom_feed.hainan
    elif project == pp_id.xiamen:
        return recom_feed.xiamen
    elif project == pp_id.fuzhou:
        return recom_feed.fuzhou
    elif project == pp_id.huzhou:
        return recom_feed.huzhou
    elif project == pp_id.nanjing:
        return recom_feed.nanjing
    elif project == pp_id.chengdu:
        return recom_feed.chengdu
    elif project == pp_id.kunming:
        return recom_feed.kunming
    elif project == pp_id.qingdao:
        return recom_feed.qingdao

class web_feed_id:
    pass


def get_name(project):
    if project == pp_id.xian:
        return "西安"
    elif project == pp_id.hainan:
        return "海南"
    elif project == pp_id.xiamen:
        return "厦门"
    elif project == pp_id.fuzhou:
        return "福州"
    elif project == pp_id.huzhou:
        return "湖州"
    elif project ==pp_id.nanjing:
        return "南京"
    elif project ==pp_id.chengdu:
        return "成都"
    elif project == pp_id.kunming:
        return "昆明"
    elif project == pp_id.qingdao:
        return "青岛"

def get_feed_id(project):
    if project == pp_id.xian:
        return feed_id.xian
    elif project == pp_id.hainan:
        return feed_id.hainan
    elif project == pp_id.xiamen:
        return feed_id.xiamen
    elif project == pp_id.fuzhou:
        return feed_id.fuzhou
    elif project == pp_id.huzhou:
        return feed_id.huzhou
    elif project == pp_id.qingdao:
        return feed_id.qingdao
    elif project ==pp_id.nanjing:
        return feed_id.nanjing
    elif project == pp_id.chengdu:
        return feed_id.chengdu
    elif project ==pp_id.kunming:
        return feed_id.kunming
