import re ,json
from Api_Server.Support.Base_Compare import *
from Api_Server.Asert.asert import *
from Api_Repository.Data_Center.Entity import *

#  模板 key   ；  输出样式

@asert_success
def keyValue_ToString_byIndex(data,key_list,by_index ,template_print='key=value  |   key'):
    '''

    :param data:  {'_isSuccess': True, '_msg': '接口请求成功', 'data': data}
    :param key_list:
    :param by_index:
    :param template_print:
    :return:
    '''
    re_list=[]
    _template_print_list = _get_log_string(template_print)
    k_v = _template_print_list[0]
    k_k = _template_print_list[1]
    if type(data["data"]) == list:
        for index,_dict in enumerate(data["data"]):
            re_dict={}
            if index +1 not in by_index:
                continue
            print('第'+str(index+1)+'行：',end='')
            for key in key_list:
                temp = map(_dict, key ,default="无值")
                print(key, k_v, temp , k_k,end='')
                re_dict.update({key : temp})
            re_list.append(re_dict)
            print('')
        data["data"] = re_list
    else:
        print("请检查输入的值是否为list")
        data["data"] = None


    return data

@asert_success
def keyValues_ToString(data,key_list,template_print='key=value  |   key'):
    '''

    :param data:  {'_isSuccess': True, '_msg': '接口请求成功', 'data': data}
    :param key_list:
    :param template_print:
    :return:      {'_isSuccess': True, '_msg': '接口请求成功', 'data': re_dict }
    '''

    _template_print_list = _get_log_string(template_print)
    k_v = _template_print_list[0]
    k_k = _template_print_list[1]

    if type(data["data"]) == dict:
        re_dict = {}
        for key in key_list:
            temp = map(data["data"] ,key,default="无值")
            print(key,k_v,temp ,k_k ,end='')
            re_dict.update({key ,temp})
        print('')
        data["data"] = re_dict
        return data

    elif type(data["data"]) == list:
        re_list =[]
        for index,_dict in enumerate(data["data"]):
            temp_dict = {}
            print('第'+str(index+1)+'行：',end='')
            for key in key_list:
                temp = map(_dict, key ,default="无值")
                print(key, k_v, temp , k_k,end='')
                temp_dict.update({key : temp })

            #兼容广告
            if _dict.get("itemType" ,None) ==0:
            # if _dict["itemType"] == 0:
                temp=map(_dict["templateMaterial"]["adJsonContent"],"title","无值")
                print("title", k_v, temp, k_k, end='')
                temp_dict.update({"title": temp})
            re_list.append(temp_dict)
            print('')

        data["data"] = re_list
        return data

    else:
        data["data"] = None
        return data


@asert_success
def keyValues_ToString_byType(data,template_print='key=value  |   key'):
    '''
        根据类型输出 类型，标题，等
    :param data:  {'_isSuccess': True, '_msg': '接口请求成功', 'data': data}
    :param template_print:
    :return:      {'_isSuccess': True, '_msg': '接口请求成功', 'data': re_dict }
    '''
    pass

def _get_value_byType(data):
    _type = str(data["itemType"])
    if itemType.article == _type :
        pass
    elif itemType.discussion == _type :
        pass
    elif itemType.topic == _type :
        pass
    elif itemType.video == _type :
        pass
    elif itemType.guanggao == _type :
        pass
    elif itemType.kaikecolum == _type :
        pass



def _get_log_string(template_print):
    p1 = r"y.+?v"
    p2 = r"ue.+?k"
    pattern1 = re.compile(p1)
    pattern2 = re.compile(p2)
    return [pattern1.findall(template_print)[0][1:-1],pattern2.findall(template_print)[0][2:-1]]





if __name__ == '__main__':
    import requests
   #取名为re会与正则表达式重命名
    # rep=requests.get(url='https://36kr.com/pp/api/newsflash?project_id=1')
    # data=get_dict(rep.json())





    # keyValue_ToString_byIndex(data  ,key_list=['id','title'] ,by_index=[7])
    # KeyValues_ToString(data, key_list=['id', 'title'])