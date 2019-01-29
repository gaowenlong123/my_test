from Api_Server.Support.Base_Time import *
from Api_Server.Root_Gateway.Base_Md5 import *
from Api_Server.Support.Base_Enums import *


def App_request(data , environment=0):
    '''

    :param data: { 参数  ， 访问地址}  通过参数来控制访问的路径
    :param environment:  0 是测试环境  ，  1 是线上
    :return:
    '''
    sign = MD5(data)

    if environment==0:
        _url =  Enums.test_App_url_java + data["address"]
    else:
        _url = Enums.App_url_java + data["address"]

    header = {
        # "Accept": "application/json",
        "timestamp": str(time_Stamp()),
        "Content-Type": "application/json;charset=utf-8",
        # "User-Agent": "36kr-iOS/8.1.2 (unknown); Build 665; iOS 12.0.1; Scale/2.0;",
        # "Connection": "keep-alive",
        # "device": "5C310F42-EFB0-41CA-8291-9ED0CCFFF2A4",
        # "Cookie": "kr_device_id=5C310F42-EFB0-41CA-8291-9ED0CCFFF2A4; kr_device_id.sig=YySiPNKgIDOGSvhgR-iPQIggDiArRzZt5aQfLKjnktE; kr_pinyou_device_uuid=5C310F42-EFB0-41CA-8291-9ED0CCFFF2A4; kr_pinyou_device_uuid.sig=UYeekVIScdBY8roccjeHbkMfqPOKT7cvj6gKGhCLzZU; krnewsfrontss=e2760ca92a18712dadf9c49a24266f48; krnewsfrontss.sig=uKSeaHNAgjmDFqy5Xn337KbbJ_oEpR1YdiwR79hhw-o; M-XSRF-TOKEN=27e32fec678ab4625e27d7dbd53fc07a895586c816c93be595e032bfd13b4050; kr_plus_id=19812349; device-uid=17a5d420-133c-11e9-a49c-dd9346f840fb",
        # "sign": sign,
    }
    rep=requests.post(url=_url+sign  , headers =header , data=json.dumps(data))
    # print(rep.status_code)
    return rep.json()