def asert_property(data ,target_data ,property ,property_value=''):
    '''
    例如 1 (data , target_data ,"id" )
         2  (data , target_data ,"state" ，property_value="offline")
    :param data:  创建时的数据
    :param target_data: 接口中拿出来的数据
    :param property:   比较的Key值
    :param property_value: 这个值，不为空，就是创建时没有数据，需要与这个指定的值对比。例如“state”
    :return:
    '''
    if target_data["_isSuccess"] == False:
        return {"result":False ,"msg":target_data["_msg"]}


    # 一般data是一个list ，当然一般只有一个 ,做了兼容
    target_temp = target_data["data"]
    if type(target_temp) == list:
        if len(target_temp)==1:
            if target_temp[0].get(property, None) != None:
                _target_data = target_data["data"][0][property]
            else:
                _target_data = 'attention ：接口值为空'
            # _target_data=target_data["data"][0][property]
        else:
            #多个比较
            _target_data='attention ：传入多个值或无值'
    else:
        if target_temp.get(property , None)!=None:
            _target_data=target_temp[property]
        else:
            _target_data = 'attention ：接口值为空'


    if property_value == "":
        if data.get(property , None) !=None:
            _data = data[property]
        else:
            _data='attention ：初始值为空'


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
        return {"result":False ,"msg":target_data["_msg"]}

    _dict = asert_property(data , target_data ,"id" )
    if _dict["result"] == False:
        return _dict
    else:
        return  asert_property(data ,target_data ,property ,property_value)


def _Bolean_ToString(real, interface, isEqual =True):
    if isEqual:
        return "原本的值："+str(real) + " 等于 " + "接口中的值" + str(interface)
    else:
        return "原本的值：" + str(real) + " 不等于 " + "接口中的值" + str(interface)
