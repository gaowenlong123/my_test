from Api_Server.Support.Base_APP import *


def channel_data(Cdata = channel_param.recom):

    data = {

        "partner_version": "8.1.2",
        "device_id": "5C310F42-EFB0-41CA-8291-9ED0CCFFF2A4",
        "param": {
            "homeCallback": "JzQmLJdikVXoNSJlJLPdIwyjXg0f4_USYiLJbNu85ZCv4y_Dou1dzKniXhz7BhvMgnG_xdCylDuovTeDnXBTEQ7qMGyGdwVyJAC4rCa-ZWMcDtQ3Op8FAIfRBe1TDQXJlPGuJh6UxO0jfTxvzwxPUQP_IdAnJWmTI8WxIYfSwXIXFfpeM40YAI5orZhLAZ9TMJeHXO2lIrbpMRwdZr3suZ1DN4DQA1ucAUceevvLxD0Bv8j1zyr7NCooErtyypme",
            "pageEvent": "0",
            "pageSize": "20",
            "platformId": "1",
            "siteId": "1",
            "subnavId": "",
            "subnavNick": "",
            "subnavType": "1"
        },
        "os_version": "12.0.1",
        "partner_id": "ios",
        "timestamp_period": "300"
    }

    for key in Cdata:
        data["param"][key]=Cdata[key]

    data.update({"address" : url.channel_feed})
    return data


def focus_data(Cdata = channel_param.recom):
    data={
	    "device_id": "5C310F42-EFB0-41CA-8291-9ED0CCFFF2A4",
	    "partner_version": "8.1.2",
	    "partner_id": "ios",
	    "param": {
		    "subnavId": "",
		    "homeCallback": "JzQmLJdikVXoNSJlJLPdIwyjXg0f4_USYiLJbNu85ZCv4y_Dou1dzKniXhz7BhvMgnG_xdCylDuovTeDnXBTEQ7qMGyGdwVyJAC4rCa-ZWMcDtQ3Op8FAIfRBe1TDQXJlPGuJh6UxO0jfTxvzwxPUQP_IdAnJWmTI8WxIYfSwXIXFfpeM40YAI5orZhLAZ9TMJeHXO2lIrbpMRwdZr3suZ1DN4DQA1ucAUceevvLxD0Bv8j1zyr7NCooErtyypme",
		    "subnavType": 1,
		    "platformId": "1",
		    "siteId": "1",
		    "subnavNick": ""
	    },
	    "timestamp_period": "300",
	    "os_version": "12.0.1"
    }

    for key in Cdata:
        data["param"][key]=Cdata[key]

    data.update({"address" : url.channel_focus})
    return data


def discovery_data():
    data={
	    "device_id": "5C310F42-EFB0-41CA-8291-9ED0CCFFF2A4",
	    "partner_version": "8.1.2",
	    "partner_id": "ios",
	    "param": {
		    "pageSize": 20,
		    "pageEvent": 0,
		    "siteId": "1",
		    "platformId": "1"
	    },
	    "timestamp_period": "300",
	    "os_version": "12.0.1"
    }

    # for key in Cdata:
    #     data["param"][key] = Cdata[key]

    data.update({"address": url.discovery_feed})
    return data


def discovery_focus():
    '''
    这个是接口包含唠嗑的数据
    :return:
    '''
    data = {
	    "device_id": "5C310F42-EFB0-41CA-8291-9ED0CCFFF2A4",
	    "partner_version": "8.1.2",
	    "partner_id": "ios",
	    "param": {
		    "platformId": "1",
		    "siteId": "1"
	    },
	    "timestamp_period": "300",
	    "os_version": "12.0.1"
    }

    # for key in Cdata:
    #     data["param"][key] = Cdata[key]

    data.update({"address": url.discovery_focus})
    return data



def copartner_data():
    data={
	    "device_id": "5C310F42-EFB0-41CA-8291-9ED0CCFFF2A4",
	    "partner_version": "8.1.2",
	    "partner_id": "ios",
	    "param": {
		    "pageSize": 20,
		    "pageEvent": 0,
		    "siteId": "1",
		    "platformId": "1"
	    },
	    "timestamp_period": "300",
	    "os_version": "12.0.1"
    }

    # for key in Cdata:
    #     data["param"][key] = Cdata[key]

    data.update({"address": url.copartner_feed})
    return data


def daysign_feed(isFeed=True):

    data={
	    "device_id": "5C310F42-EFB0-41CA-8291-9ED0CCFFF2A4",
	    "partner_version": "8.1.2",
	    "partner_id": "ios",
	    "param": {
		    "platformId": "1",
		    "siteId": "1"
	    },
	    "timestamp_period": "300",
	    "os_version": "12.0.1"
    }

    if isFeed:
        data["param"].update({"pageSize": 20})
        data["param"].update({ "pageEvent": 0})
        data.update({"address": url.daysign_feed})
    else:
        data.update({"address": url.daysign})

    # for key in Cdata:
    #     data["param"][key] = Cdata[key]

    return data

def  topic_data(isChosen=False):
    data = {
        "device_id": "5C310F42-EFB0-41CA-8291-9ED0CCFFF2A4",
        "partner_version": "8.1.2",
        "partner_id": "ios",
        "param": {
            "platformId": "1",
            "siteId": "1"
        },
        "timestamp_period": "300",
        "os_version": "12.0.1"
    }

    if isChosen:
        data.update({"address": url.topic_chosen})
    else:
        data["param"].update({"pageSize": 20})
        data["param"].update({"pageEvent": 0})
        data.update({"address": url.topic_feed})

    # for key in Cdata:
    #     data["param"][key] = Cdata[key]

    return data

def search_data(isNone = False):
    data={
	    "device_id": "5C310F42-EFB0-41CA-8291-9ED0CCFFF2A4",
	    "partner_version": "8.1.2",
	    "partner_id": "ios",
	    "param": {
		    "searchWord": "36",
		    "platformId": "1",
		    "siteId": "1"
	},
	    "timestamp_period": "300",
	    "os_version": "12.0.1"
    }

    if isNone == True:
        data["param"]["searchWord"] = "谈谈坎坎坷坷实话实说噢噢噢噢"

    data.update({"address": url.search_feed})
    return data

def search_ByType(Cvalue  ,isNone = False):
    data={
	    "device_id": "5C310F42-EFB0-41CA-8291-9ED0CCFFF2A4",
	    "partner_version": "8.1.2",
	    "partner_id": "ios",
	    "param": {
		    "searchWord": "36",
		    "platformId": "1",
		    "pageEvent": 0,
		    "sort": "date",
		    "searchType": "",
		    "siteId": "1",
		    "pageSize": 20
	    },
	    "timestamp_period": "300",
	    "os_version": "12.0.1"
    }

    if isNone == True:
        data["param"]["searchWord"] = "谈谈坎坎坷坷实话实说噢噢噢噢"

    data["param"]["searchType"] = Cvalue
    data.update({"address": url.searchType_feed})
    return data



#要不要
def get_data(self):
    # 非频道的通用数据解决
    _param = {}

    _post_data = {
        "partner_id": "ios",
        "partner_version": self.version,
        # "device_id": "92772661-C750-433A-9024-55CB605FDFFC",
        "param": _param,
    }
    return _post_data


if __name__ == '__main__':
    from Api_Server.Root_Gateway.Base_log import *
    start_log()