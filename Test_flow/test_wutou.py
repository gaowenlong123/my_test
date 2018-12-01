from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from  selenium.webdriver.support.ui import WebDriverWait
import time
# 创建chrome浏览器驱动，无头模式
chrome_options = Options()
chrome_options.add_argument('--headless')
# driver = webdriver.Chrome(chrome_options=chrome_options)
driver =webdriver.Chrome()

driver.get("https://www.36kr.com/")
driver.maximize_window()
print(driver.title)
print(driver.get_cookie('M-XSRF-TOKEN'))
# driver.close()

def find(driver,name='',t=10):
    return  WebDriverWait(driver ,t).until(lambda x:x.find_element_by_class_name(name))

def find_xpath(driver,xpath='',t=10):
    return WebDriverWait(driver, t).until(lambda x: x.find_element_by_xpath(xpath))

def yin():
    try:
        # 新手引导  先找登录，点不了就进行直接登录
        find_xpath(driver,'/html/body/div[2]/div/div[1]/div/div[6]').click()
        find(driver,'close').click()
    except:
        print('直接登录吧')

yin()



find(driver,name='login').click()
driver.find_element_by_class_name('account').send_keys('18637527151')
driver.find_element_by_class_name('password').send_keys('gao123456')
find_xpath(driver,xpath='/html/body/div[2]/div/div/div/section/button').click()



find_xpath(driver,xpath='//*[@id="app"]/div/div[1]/div/div/div[1]/img').click()
a=find_xpath(driver ,xpath='//*[@id="app"]/div/div[1]/div/div/div[1]/div/a[1]')
print('a' ,a.text)

print('login====',driver.get_cookie('M-XSRF-TOKEN'))



#1 伪装成不同ip 来避免画动图片
#2 抓到头像名称，证明已经登录状态
#3 拼接cokkie  请求接口


