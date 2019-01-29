class version:
    V8_1='8.1'
    V8_0='8.0'
    V8_1_dev='8.1.0dev'
    V8_1_2='8.1.2'
    V8_2 = '8.2_dev'


#同一一下，前面加/
class url:
    channel_feed= '/api/mis/nav/home/subnav/flow?sign='
    channel_focus='/api/mis/nav/home/subnav/recom?sign='
    discovery_feed = '/api/mis/nav/discover/flow?sign='
    discovery_focus = '/api/mis/nav/discover/recom?sign='
    copartner_feed='/api/mis/nav/copartner/flow?sign='
    daysign='/api/mis/dailyword?sign='
    daysign_feed='/api/mis/dailyword/list?sign='
    topic_feed='/api/mis/nav/search/topicList?sign='
    topic_chosen='/api/mis/nav/search/recom?sign='
    search_feed='/api/mis/nav/search/result?sign='
    searchType_feed= '/api/mis/nav/search/resultbytype?sign='


class channel_param:
    def get_all(filter='_'):
        re_dict={}
        for name, value in vars(channel_param).items():
            if "_" not in name :
                # print(name, value)
                re_dict.update({name:value})
        # print(re_dict)
        return re_dict


    recom = {
        "subnavId": "59",
        "subnavNick": "recommend",
    }

    video = {
        "subnavId": "290",
        "subnavNick": "video",
    }

    audio = {
        "subnavNick": "audio",
        "subnavId": "73",
    }

    hot = {
        "subnavId": "400",
        "subnavNick": "hotlist"
    }

    care={
        "subnavNick": "dynamic",
        "subnavId": "66",
    }

    newsflash={
        "subnavNick": "newsflash",
        "subnavId": "62",
    }

    keji = {
        "subnavNick": "keji",
        "subnavId": "105",
    }

    shenghuo = {
        "subnavNick": "shangye",
        "subnavId": "104",
    }

    zhichang = {
        "subnavNick": "zhichang",
        "subnavId": "106",
    }

    chuangtou = {
        "subnavNick": "chuangtou",
        "subnavId": "103",
    }

    chuxing = {
        "subnavNick": "chuxing",
        "subnavId": "291",
    }

    renwu = {
        "subnavNick": "renwu",
        "subnavId": "292",
    }

    shendu = {
        "subnavNick": "shendu",
        "subnavId": "108",
    }

    chuhai = {
        "subnavNick": "chuhai",
        "subnavId": "231",
    }

    city = {
        "subnavNick": "city",
        "subnavId": "293",
    }

    tanzi = {
        "subnavNick": "tanzi",
        "subnavId": "233",
    }

    blockchain = {
        "subnavNick": "blockchain",
        "subnavId": "272",
    }


    #地方站
    localxian = {
        "subnavNick": "localstation",
        "subnavId": "298",
    }
    localhainan = {
        "subnavNick": "localstation",
        "subnavId": "314",
    }
    localqingdao = {
        "subnavNick": "localstation",
        "subnavId": "315",
    }


class search_type:
    def get_all(filter='_'):
        re_dict={}
        for name, value in vars(search_type).items():
            if "_" not in name :
                # print(name, value)
                re_dict.update({name:value})
        # print(re_dict)
        return re_dict

    video='video'
    newsflash='newsflash'
    article='article'
    audio='audio'
    author='author'


if __name__ == '__main__':
    data1=search_type.get_all()


