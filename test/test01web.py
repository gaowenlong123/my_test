from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from  selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
# 创建chrome浏览器驱动，无头模式
chrome_options = Options()
# chrome_options.add_argument('--headless')


# 设置代理
# chrome_options.add_argument("--proxy-server=http://202.20.16.82:10152")
# 一定要注意，=两边不能有空格，不能是这样--proxy-server = http://202.20.16.82:10152

# driver = webdriver.Chrome(chrome_options=chrome_options)
driver =webdriver.Chrome()
print(driver.get('http://httpbin.org/ip'))
print(driver.page_source)
# driver.get("https://www.36kr.com/")
driver.get('http://test01web.36kr.com/')
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
driver.find_element_by_class_name('account').send_keys('23322228888')
driver.find_element_by_class_name('password').send_keys('er2222')
find_xpath(driver,xpath='/html/body/div[2]/div/div/div/section/button').click()

# a=input('please input any')
#人工睡一会？？



move=find_xpath(driver,xpath='//*[@id="app"]/div/div[1]/div/div/div[1]')
ActionChains(driver).move_to_element(move).click().perform()
a=find_xpath(driver ,xpath='//*[@id="app"]/div/div[1]/div/div/div[1]/div/a[1]')
print('username = ' ,a.text)  #登录成功
if a.text != '自动化小能手':
    time.sleep(5)


#
b=find_xpath(driver ,xpath='//*[@id="app"]/div/div[2]/div/ul/li[2]/div/a').click()
# ActionChains(driver).move_to_element(b).click().perform()
print('login====',driver.get_cookie('M-XSRF-TOKEN'))


#获得cookie
cok=driver.get_cookies()
Cookie=''
for i in cok:
    print(i[ 'name'] ,'  ====  ',end=' ')
    print(i['value'])
    Cookie +=i['name']+'='+i['value']+';'

print(Cookie)
print('--------------------------')
print(Cookie[:-1])


header={
    'M-X-XSRF-TOKEN':driver.get_cookie( 'M-XSRF-TOKEN')['value'],
   'Cookie' :Cookie,
}
# post_data={"ltype":"post","lid":5161738,"direction":"plus"}


post_data={"ctype":"post","cid":10464741,"content":"dd"}

import requests
re =requests.session()
# print(re.cookies)
# res=re.post(url='https://36kr.com/pp/api/like' ,headers=header ,data=post_data)
# print(res.cookies)

for i in range(100):
    post_data['content'] = 'dd' + str(i)
    res=re.post(url='https://test02.36kr.com/pp/api/comment' ,headers=header ,data=post_data)
    print(res.text)
    time.sleep(2)