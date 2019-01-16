
def asert_property(data ,target_data ,property ,property_value=''):

    if target_data["_isSuccess"] == False:
        print(target_data["_msg"])
        return {"result":False ,"msg":target_data["_msg"]}

    # print("attention 这里是一个list，注意")
    _target_data=target_data["data"][0][property]

    if property_value == "":
        _data = data[property]
        # print("attention 这里只是一个简单字典")
        if _data == _target_data:
            return {"result":True ,"msg":_Bolean_ToString(_data ,_target_data ,isEqual=True)}
        else:
            return {"result": False, "msg": _Bolean_ToString(_data ,_target_data ,isEqual=False)}
    else:
        if property_value == _target_data:
            return {"result":True ,"msg":_Bolean_ToString(property_value ,_target_data ,isEqual=True)}
        else:
            return {"result": False, "msg":_Bolean_ToString(property_value ,_target_data ,isEqual=False)}

def asert_property_ById(data ,target_data ,property ,property_value=''):

    if target_data["_isSuccess"] == False:
        print(target_data["_msg"])
        return {"result":False ,"msg":target_data["_msg"]}

    _dict = asert_property(data , target_data ,"id" )
    if _dict["result"] == False:
        return _dict
    else:
        return  asert_property(data ,target_data ,property ,property_value)





def _Bolean_ToString( shiji , feed ,isEqual =True):
    if isEqual:
        return "原本的值："+str(shiji)+" 等于 "+"接口中的值"+str(feed)
    else:
        return "原本的值：" + str(shiji) + " 不等于 " + "接口中的值" + str(feed)

