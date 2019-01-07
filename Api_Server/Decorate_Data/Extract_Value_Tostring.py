import re
from Api_Server.Support.Base_Compare import *
#  模板 key   ；  输出样式


def keyValue_ToString_byIndex(data,key_list,by_index ,template_print='key=value  |   key'):
    _re_list=[]
    _template_print_list = _get_log_string(template_print)
    k_v = _template_print_list[0]
    k_k = _template_print_list[1]
    if type(data) == list:
        for index,_dict in enumerate(data):
            if index +1 not in by_index:
                continue
            print('第'+str(index+1)+'行：',end='')
            for key in key_list:
                temp = map(_dict, key ,default="无值")
                print(key, k_v, temp , k_k,end='')
                _re_list.append(temp)
            print('')

            return _re_list
    else:

        print("请检查输入的值是否为list")
        return _re_list

def keyValues_ToString(data,key_list,template_print='key=value  |   key'):
    _template_print_list = _get_log_string(template_print)
    k_v = _template_print_list[0]
    k_k = _template_print_list[1]

    if type(data) == dict:
        for key in key_list:
            print(key,k_v,map(data ,key,default="无值"),k_k ,end='')
        print('')

    elif type(data) == list:
        for index,_dict in enumerate(data):
            print('第'+str(index+1)+'行：',end='')
            for key in key_list:
                print(key, k_v, map(_dict, key ,default="无值"), k_k,end='')
            print('')
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
    rep=requests.get(url='https://36kr.com/pp/api/newsflash?project_id=1')
    # data=get_dict(rep.json())





    # keyValue_ToString_byIndex(data  ,key_list=['id','title'] ,by_index=[7])
    # KeyValues_ToString(data, key_list=['id', 'title'])