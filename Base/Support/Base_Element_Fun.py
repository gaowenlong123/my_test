from  selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class  Function():
    def __int__(self):
        pass

    def find_xpath(self ,driver ,xpath=''):
        return WebDriverWait(driver , 15).until(lambda  x : x.find_element_by_xpath(xpath))

    def find_id(self , driver , id =''):
        return WebDriverWait(driver , 15).until(lambda  x : x.find_element_by_id(id))

    def find_class_name(self ,driver ,class_name=''):
        return WebDriverWait(driver, 15).until(lambda x: x.find_element_by_class_name(class_name))