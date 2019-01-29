# 登录的地方是哪个
from Api_Server.Base.Base_Text import read_text

class Enums:

    #线上
    Web_url = 'https://www.36kr.com/'

    App_url_java = 'http://gateway.36kr.com'

    App_url_php= 'https://36kr.com/pp/api'

    Cms_url = ''



    #测试
    test_Web_url='http://test01web.36kr.com/'

    test_Cms_url = 'http://cmstest02.36kr.com/'

    test_Mrs_url='http://ssotest27.36kr.com/login'   #登录页面

    test_App_url_java= 'http://gatewaytest36.36kr.com'


    #路径
    # 把文件Api_Server\Root\Cookie.pickle 本机路径填写下面
    cookie_path='E:\Pycharm_Git\my_test\Api_Server\Root\Cookie.pickle'

    password= read_text('C:\\Users\\Administrator\\Desktop\\password.txt')


if __name__ == '__main__':
    pass


