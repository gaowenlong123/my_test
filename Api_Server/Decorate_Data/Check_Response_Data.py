
def check_request(data):
    if data.get('code' ,None) != None:
        if str(data["code"]) != "0":
            return {"_isSuccess":False,"_msg":'接口请求失败'}
        else:
            return {"_isSuccess":True,"_msg":'接口请求成功'}
    else:
            return {"_isSuccess":False,"_msg":'http请求失败'}


def check_data(data ,key):
    if data.get(key ,None) == None:
            return '接口返回值有误，请重新输入Key值'
    return data[key]



if __name__ == '__main__':

    a={"msg":"签名错误，服务端待签名字符串:{\"partner_id\": \"ios\", \"partner_version\": \"8.1\", \"param\": {\"platformId\": \"1\", \"siteId\": \"1\", \"feedId\": 196}}","code":"1"}
    print(check_data(a,"a1"))