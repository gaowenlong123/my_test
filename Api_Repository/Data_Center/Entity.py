class feed_id:
    tj="59"
    bzsj="357"

    hainan="314"
    xian="298"
    nanjing="300"
    chengdu="301"
    kunming="302"

class pp_id:
    xian = 86
    nanjing = 87
    chengdu = 88
    kunming = 89

class recom_feed:
    tuijian="{\"feed_ids\":[59]}"

    #地方站
    xianan = "{\"feed_ids\":[298]}"

def local_recom_feed(project):
    if project == 86:
        return recom_feed.xianan
    elif project == 87:
        return ''
    elif project == 88:
        return ''
    elif project == 89:
        return ''

class web_feed_id:
    pass