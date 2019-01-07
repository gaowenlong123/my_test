from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Api_Server.Support.Base_Enums import Enums
from Api_Server.Base.Base_Login import Login


class WebDriver():
    def __init__(self,para=''):
        self.user ={'account':'23322228888' ,'pass':'er2222','name':'自动化小能手'}
        self.jira_user={'account':'jira' ,'pass':'123456','name':'jira'} #????
        self.driver=None
        self.ip=''

        self.chrome_options = Options()
        self.login_action = Login()

    def login(self,login_type=Enums.test_Web_url, is_headless =False ,is_proxy=False ):

        self.is_headless = is_headless
        self.is_proxy = is_proxy
        self.login_type = login_type

        # 启动浏览器
        if self.is_headless:
            self._Chrome_HeadLess(self.is_proxy)
        else:
            self._Chrome(self.is_proxy)

        self._get_current_ip()

        if Enums.test_Web_url== self.login_type:
            self.driver=self.login_action.Web_Login(self.driver ,user=self.user)
        elif Enums.test_Cms_url == self.login_type:
            self.driver=self.login_action.Cms_Login(self.driver ,user=self.user)
        elif Enums.test_Mrs_url == self.login_type:
            self.driver = self.login_action.Mrs_Login(self.driver ,user=self.user)
        else:
            print('interface 输入的url不正确')



    def _Chrome_HeadLess(self ,is_proxy):
        '''  返回driver'''
        if is_proxy:
            self._set_proxy()
        self.chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(chrome_options=self.chrome_options)
        # return self.driver

    def _Chrome(self,is_proxy):
        if is_proxy:
            self._set_proxy()
        self.driver = webdriver.Chrome()
        # return self.driver

    def _set_proxy(self):
        # 设置代理,访问一次，变化一次
        ip="???"
        proxy="--proxy-server="+ip
        self.chrome_options.add_argument(proxy)
        # chrome_options.add_argument("--proxy-server=http://202.20.16.82:10152")
        # 一定要注意，=两边不能有空格，不能是这样--proxy-server = http://202.20.16.82:10152

    def _get_current_ip(self ):
        self.driver.get('http://httpbin.org/ip')
        page=self.driver.page_source

        print('ip = ' ,'')
        self.ip = ''
        #需要处理一下

    def _get_Cookie(self):
        temp = self.driver.get_cookies()
        print(temp)
        Cookie = ''
        for i in temp:
            print(i['name'], '  ====  ', end=' ')
            print(i['value'])
            Cookie += i['name'] + '=' + i['value'] + ';'

        # self.Cookie=Cookie[:-1]
        return Cookie[:-1]





    def get_headers_Token(self):
        headers = {
            'M-X-XSRF-TOKEN': self.driver.get_cookie('M-XSRF-TOKEN')['value'],
            'Cookie': self._get_Cookie(),
        }
        return headers

    def get_headers(self):
        headers = {
            'Cookie': self._get_Cookie(),
        }
        return headers

    def get_Cookie(self):
        return self._get_Cookie()

    def get_Token(self):
        return self.driver.get_cookie( 'M-XSRF-TOKEN')['value']

    def kill_driver(self):
        self.driver.close()
        self.driver.quit()

    def get_driver(self):
        return self.driver

    def get_Current_url(self):
        return self.driver.current_url

    def get_ip(self):
        return self.ip