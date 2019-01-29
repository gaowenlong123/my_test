
def asert_http(data):
    if data.get("code" ,None) != None:
        if str(data["code"]) == "0":
            return True
        else:
            return data["msg"]
    else:
        return "http请求失败"



if __name__ == '__main__':
    pass
