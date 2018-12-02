from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class WebDriver():
    def __int__(self ,login_type, is_headless =False ,is_proxy=False ):
        self.driver=None
        self.chrome_options = Options()

        #启动浏览器
        if is_headless :
            self.Chrome_HeadLess(is_proxy)
        else:
            self.Chrome(is_proxy)

        if login_type=='web':
            self.web_login()


    def web_login(self):
        pass

    def Chrome_HeadLess(self ,is_proxy):
        '''  返回driver'''
        if is_proxy:
            self.set_proxy()
        self.chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(chrome_options=self.chrome_options)
        return self.driver


    def set_proxy(self):
        # 设置代理,访问一次，变化一次
        ip="???"
        proxy="--proxy-server="+ip
        self.chrome_options.add_argument(proxy)
        # chrome_options.add_argument("--proxy-server=http://202.20.16.82:10152")
        # 一定要注意，=两边不能有空格，不能是这样--proxy-server = http://202.20.16.82:10152

    def Chrome(self,is_proxy):
        if is_proxy:
            self.set_proxy()
        self.driver = webdriver.Chrome()
        return self.driver


    def get_current_ip(self , driver):
        self.driver.get('http://httpbin.org/ip')
        page=self.driver.page_source
        #需要处理一下



    def get_Cookie(self):
        pass

    def get_headers(self):
        pass