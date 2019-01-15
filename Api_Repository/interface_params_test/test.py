# 伪装请求gateway
#第二次请求会失败 ？？
#那就请求一次new一次吧。
#1 ：形成headers   2：收集data  3：生成测试用例
from Api_Server.Root.Gateway import *
from Api_Server.Decorate_Data.Extract_Value_Tostring import *
from Api_Server.Decorate_Data.Extract_Dict_Value import *
from Api_Server.Support.Base_Time import *



data={

	"partner_version": "8.1.2",
	# "device_id": "5C310F42-EFB0-41CA-8291-9ED0CCFFF2A4",
	"param": {
		"homeCallback": "JzQmLJdikVXoNSJlJLPdI60raNP2D1ysJ9XY-fO8Q7-MFRORsFB3fANVERVVgu_YiCMzk6el430Hfl8EmntSfaQJdjXB-4kyOwBPAr8oGfJ9Sc2C91b_7rHzfVMcBRXDOE0LLGO7HK05wBMeS3PveEv-7TV7GfaBJKdzeAUMnIANpOduYtIMVj-OeN4JwuG2UkHT1-8b162MTDwF5lkzmQ",
		"subnavId": 400,
		"pageSize": 20,
		"platformId": "1",
		"pageEvent": 0,
		"siteId": "1",
		"subnavType": 1,
		"subnavNick": "hotlist"
	},
	"os_version": "12.0.1",
	"partner_id": "ios",
	# "timestamp_period": "1"
}



import requests ,json ,hashlib


def MD5(body):
    _md5 =hashlib.md5()
    pass_word = body + read_text(Enums.password_path)
    _md5.update(pass_word.encode('utf-8'))
    sign = _md5.hexdigest()
    return sign



def rep():


    sign = MD5(json.dumps(data))
    header = {
        # "Accept": "application/json",
        # "timestamp": str(time_Stamp()),
        "Content-Type": "application/json;charset=utf-8",
        # "User-Agent": "36kr-iOS/8.1.2 (unknown); Build 665; iOS 12.0.1; Scale/2.0;",
        # "Connection": "keep-alive",
        # "device": "5C310F42-EFB0-41CA-8291-9ED0CCFFF2A4",
        # "Cookie": "kr_device_id=5C310F42-EFB0-41CA-8291-9ED0CCFFF2A4; kr_device_id.sig=YySiPNKgIDOGSvhgR-iPQIggDiArRzZt5aQfLKjnktE; kr_pinyou_device_uuid=5C310F42-EFB0-41CA-8291-9ED0CCFFF2A4; kr_pinyou_device_uuid.sig=UYeekVIScdBY8roccjeHbkMfqPOKT7cvj6gKGhCLzZU; krnewsfrontss=e2760ca92a18712dadf9c49a24266f48; krnewsfrontss.sig=uKSeaHNAgjmDFqy5Xn337KbbJ_oEpR1YdiwR79hhw-o; M-XSRF-TOKEN=27e32fec678ab4625e27d7dbd53fc07a895586c816c93be595e032bfd13b4050; kr_plus_id=19812349; device-uid=17a5d420-133c-11e9-a49c-dd9346f840fb",
        # "sign": sign,
    }
    rep=requests.post(url="http://gatewaytest36.36kr.com/api/mis/nav/home/subnav/flow?sign="+sign  , headers =header , data=json.dumps(data))
    print(rep.text)
    return rep.status_code


for i in range(5):

    data=rep()
    print(data)
    # data1=get_dict_value(data ,template_path='data/itemList')
    print(i)

    # keyValues_ToString(data=data1, key_list=["id","widgetTitle","duration"])
    time.sleep(5)

