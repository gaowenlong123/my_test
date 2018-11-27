import yaml
import os
from yaml.scanner import ScannerError
from Base.BaseOs import change_path
from Base.str_enum import test_enum as t


def getYaml(path =''):
    try:
        with open(path , encoding='utf-8') as f:
            app=yaml.load(f)
            print("TSTE==============",app)
            return [True ,app]
    except FileNotFoundError:
        print('error===>用例文件不存在')

        app={ t.check: [{t.element_info: '', t.operate_type: 'get_value', t.find_type: 'ids', t.info: '用例文件不存在'}],
              t.testinfo: [{t.title: '',t.id: '', t.info: ''}],
              t.testcase: [{t.element_info: '', t.info: '', t.operate_type: '', t.find_type: ''},
                            {t.element_info: '', 'msg': '', t.operate_type: '', t.find_type: '', t.info: ''},
                           {t.element_info: '', 'msg': '', t.operate_type: '', t.find_type: '', t.info: ''},
                            {t.element_info: '', t.info: '', t.operate_type: '', t.find_type: ''}]}

        return [False ,app]

    except ScannerError :
        print('error ===> yaml格式不正确')

        app = {t.check: [{t.element_info: '', t.operate_type: 'get_value', t.find_type: 'ids', t.info: 'yaml格式不正确'}],
               t.testinfo: [{t.title: '', t.id: '', t.info: ''}],
               t.testcase: [{t.element_info: '', t.info: '', t.operate_type: '', t.find_type: ''},
                            {t.element_info: '', 'msg':'', t.operate_type: '', t.find_type: '', t.info: ''},
                            {t.element_info: '', 'msg': '', t.operate_type: '', t.find_type: '', t.info: ''},
                            {t.element_info: '', t.info: '', t.operate_type: '', t.find_type: ''}]}

        return [False , app]




if __name__ == '__main__':
    path=change_path()
    print(path)
    print(getYaml(path))

