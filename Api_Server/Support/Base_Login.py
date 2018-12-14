from Api_Server.Support.Base_Enums import Enums
from Api_Server.Support.Base_Element_Fun import Function
from selenium.webdriver.common.action_chains import ActionChains
import time


#登录的页面逻辑

class Login():
    def __init__(self):

        self.Func = Function()

    def Web_Login(self , driver ,user  ):
        driver.get(Enums.test_Web_url)
        driver.maximize_window()
        print('未登录之前的Token  ： ',driver.get_cookie('M-XSRF-TOKEN'))

        self.web_guide(driver)

        self.Func.find_class_name(driver, 'login').click()
        self.Func.find_class_name(driver,'account').send_keys(user['account'])
        self.Func.find_class_name(driver,'password').send_keys(user['pass'])
        self.Func.find_xpath(driver, xpath='/html/body/div[2]/div/div/div/section/button').click()

        # a=input('please input any')   到了机器验证了
        # 人工睡一会？？

        try:
            self.Func.find_xpath(driver, xpath='//*[@id="app"]/div/div[1]/div/div/div[1]')
            for i in range(5):
                print('睡眠 ',i,' 秒')
                time.sleep(1)
        except:
            input('如果不可见，就等待输入 ')


        move = self.Func.find_xpath(driver, xpath='//*[@id="app"]/div/div[1]/div/div/div[1]')
        ActionChains(driver).move_to_element(move).click().perform()
        page_name = self.Func.find_xpath(driver, xpath='//*[@id="app"]/div/div[1]/div/div/div[1]/div/a[1]')


        print('username = ', page_name.text)  # 登录验证
        if page_name.text !=user['name']:
            time.sleep(5)
            print('username again = ', page_name.text)  # 登录验证
            if page_name.text != user['name']:
                return {'result' : False}
                                  #如果还是不为用户名，就重新登录一遍

        ele = self.Func.find_xpath(driver, xpath='//*[@id="app"]/div/div[2]/div/ul/li[2]/div/a').click()
        # ActionChains(driver).move_to_element(ele).click().perform()
        print('login success <<<--------->>> ', driver.get_cookie('M-XSRF-TOKEN'))

        return driver


    def Cms_Login(self, driver ,user):
        driver.get(Enums.test_Cms_url)
        driver.maximize_window()
        print('未登录之前的Token  ： ', driver.get_cookie('M-XSRF-TOKEN'))


        self.Func.find_xpath(driver ,xpath='//*[@id="app"]/div/div/span[2]/a').click()
        self.Func.switch_window(driver,2)
        self.Func.find_xpath(driver,xpath='//*[@id="kr-shield-username"]').send_keys(user['account'])
        self.Func.find_xpath(driver , xpath='//*[@id="kr-shield-password"]').send_keys(user['pass'])
        self.Func.find_xpath(driver , xpath='//*[@id="kr-shield-submit"]').click()

        driver.maximize_window()
        # self.Func.switch_window(driver, 1)

        # a=input('please input any')   到了机器验证了
        # 人工睡一会？？
        try:
            self.Func.find_xpath(driver, xpath='//*[@id="2$Menu"]/li[1]/a')
            for i in range(5):
                print('睡眠 ', i, ' 秒')
                time.sleep(1)
        except:
            input('如果不可见，就等待输入 ')

        self.Func.refresh(driver ,0)
        page_name = self.Func.find_xpath(driver ,xpath='//*[@id="app"]/div/div[1]/div/div[1]/span/span[1]')

        print('username = ', page_name.text)  # 登录验证
        if page_name.text != user['name']:
            time.sleep(5)
            print('username again = ', page_name.text)  # 登录验证
            if page_name.text != user['name']:
                return {'result': False}
                # 如果还是不为用户名，就重新登录一遍

        self.Func.find_xpath(driver, xpath='//*[@id="2$Menu"]/li[1]/a').click()

        print('login success <<<--------->>> ', driver.get_cookie('M-XSRF-TOKEN'))

        return driver

    def Mrs_Login(self , driver ,user):
        driver.get(Enums.test_Mrs_url)
        driver.maximize_window()
        print('未登录之前的Token  ： ', driver.get_cookie('M-XSRF-TOKEN'))
        a=input('请你手动登录，我就不搞自动化了，浪费时间=-=，登陆完输入任意值')
        self.Func.refresh(driver, 2)

        page_name = self.Func.find_xpath(driver ,xpath='//*[@id="root"]/div/div[1]/div/span/span[2]')
        if user['name'] not in page_name.text  :
            time.sleep(3)
            print('username again = ', page_name.text)  # 登录验证
            if user['name'] not in page_name.text :
                print('登录失败')
                return {'result': False}
        print('login success <<<--------->>> ', driver.get_cookie('M-XSRF-TOKEN'))

        return driver

    def web_guide(self , driver):
        try:
            # 新手引导  先找登录，点不了就进行直接登录
            self.Func.find_xpath(driver, '/html/body/div[2]/div/div[1]/div/div[6]').click()
            self.Func.find_class_name(driver, 'close').click()
        except:
            print('直接登录吧')
