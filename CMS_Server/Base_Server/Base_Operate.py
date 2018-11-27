from  selenium import  webdriver
from  selenium.webdriver.support.ui import WebDriverWait
import selenium.common.exceptions
from selenium.webdriver.common.action_chains import *
from Base.str_enum import Eunms as enum , find_type as f ,operate_type as op
import time , re

# wd = webdriver.Chrome()


class Operate_Elements():
    '''  实例时需要传入webdriver '''
    def __init__(self ,webdriver):
        self.wd = webdriver
        # self.object_list = []
        self.object=None
        self.handles=[]
        pass


    #预操作,拆解数据,预先检查数据
    def findElement(self ,operate):
        '''  执行testcase '''

        #如果没有检查时间，t 就为else 后面的值  , 并且字典不新增加值 。如果有，t 就是检查时间
        t = operate['check_time'] if operate.get('check_time' , '0') !='0' else  enum.WAIT_TIME

        try:
            if type(operate)==list:
                #多个操作
                for item in operate:
                    t = item['check_time'] if item.get('check_time' , '0') !='0' else  enum.WAIT_TIME
                    if self.is_Element(item) == None:  #操作不需要查询元素
                        return {'result': True}
                    WebDriverWait(self.wd , t).until(lambda b :  self.Element_By(item))
                    return  {'result':True}          #不需要返回list吗？ 只是检查元素

            if type(operate)==dict:
                #单个操作
                if self.is_Element(operate) == None:  # 操作不需要查询元素
                    return {'result': True}
                WebDriverWait(self.wd, t).until(lambda b : self.Element_By(operate))
                return {'result': True}

        #报错直接提示
        except selenium.common.exceptions.NoSuchElementException:
            print('BaseOperate__error===> 没用该元素')
        except selenium.common.exceptions.TimeoutException:
            print('BaseOperate__error===> 等待时间超时')
        except selenium.common.exceptions.WebDriverException:
            print('BaseOperate__error===> Webdriver出现问题')


    #操作
    def operate(self , operate, testInfo, logTest):
        result = self.findElement(operate)

        if result['result']:
            return  self.operate_by(operate, testInfo, logTest)
        else:
            return result

    # 智能等待，翻页
    def operate_by(self , operate, testInfo, logTest):
        try:
             #操作元素
            if self.is_Element(operate) != None:
                info = '%s _ %s _ %s _ %s'%(
                    operate.get('element_info' , ' '),operate.get('find_type' , ' ')
                    ,operate.get('operate_type' ,' '),operate.get('info',' ')
                )

                # logTest.buildStartLine(testInfo[0]["id"] + "_" + testInfo[0]["title"] + "_" + info)  # 记录日志

                if operate.get('operate_type' , '0') =='0':
                    return {'result' : False}

                operate_E_fun={
                    op.click:lambda  :self.click(operate),
                    op.send_keys:lambda  :self.send_keys(operate),
                    op.get_text:lambda   :self.get_text(operate),
                    op.get_value:lambda  :self.get_value(operate),
                    op.move_to_elemrnt:lambda   :self.move_to_element(operate),
                    op.get_list : lambda   : self.get_list(operate)
                }
                return operate_E_fun[operate['operate_type']]()

            #不操作元素
            else:
                info = '%s _ %s _ %s' % (
                    operate.get('element_info', ' ')
                    , operate.get('operate_type', ' '), operate.get('info', ' ')
                )

                #logTest.buildStartLine(testInfo[0]["id"] + "_" + testInfo[0]["title"] + "_" + info)  # 记录日志
                operate_fun={
                    op.switch_window:lambda  : self.switch_window(operate),
                    op.scroll_down: lambda  :self.scroll_down(operate),
                    op.scroll_up: lambda  :self.scroll_up(operate),
                    op.close_window: lambda  :self.close_window(operate),
                    op.change_size: lambda  :self.change_size(operate),
                    op.get_driver:lambda  :self.get_driver(),
                    op.sleep :lambda  :self.sleep(operate),
                    op.refresh : lambda :self.refresh(operate)
                }
                return operate_fun[operate['operate_type']]()

                # =-=
        except IndexError:
            logTest.buildStartLine(
                testInfo[0]["id"] + "_" + testInfo[0]["title"] + "_" + operate["element_info"] + "索引错误")  # 记录日志
            # print(operate["element_info"] + "索引错误")
            return {"result": False, "type": enum.INDEX_ERROR}
        except selenium.common.exceptions.NoSuchElementException:
            logTest.buildStartLine(
                testInfo[0]["id"] + "_" + testInfo[0]["title"] + "_" + operate[
                    "element_info"] + "页面元素不存在或没加载完成")  # 记录日志
            # print(operate["element_info"] + "页面元素不存在或没有加载完成")
            return {"result": False, "type": enum.NO_SUCH}
        except selenium.common.exceptions.StaleElementReferenceException:
            logTest.buildStartLine(
                testInfo[0]["id"] + "_" + testInfo[0]["title"] + "_" + operate[
                    "element_info"] + "页面元素已经变化")  # 记录日志
            # print(operate["element_info"] + "页面元素已经变化")
            return {"result": False, "type": enum.STALE_ELEMENT_REFERENCE_EXCEPTION}
        except KeyError:
            # 如果key不存在，一般都是在自定义的page页面去处理了，这里直接返回为真
            return {"result": True}


    def click(self ,operate):
        #下拉框元素我不会通过Id来拿
        #若果1是数字，就是list，如果是元素就点击一次
        #如果是driver点击还是元素对象下的点击

        #   数字表示要点击的元素列表,
        '''必须是数字,从零开始，兼容中英大小写'''
        if ','in operate['element_info'] or '，' in operate['element_info']:
            temp_list =[]
            temp=operate['element_info'].split(',')
            for str in temp:
                i = str.split('，')
                for m in i:
                    temp_list.append(m)
            # temp_list=sorted(temp_list)

            if self.object==None:
                self.Element_By(operate).click()
            else:
                for m in temp_list:
                    self.Element_By_object(operate)[m].click()
                    time.sleep(0.5)
            return {'result':True}
        else:
            if self.object == None:
                self.Element_By(operate).click()
            else:
                self.Element_By_object(operate).click()
            return {'result':True}

    def send_keys(self,operate):
        temp=self.Element_By(operate)
        temp.send_keys('.')
        temp.clear()
        temp.send_keys(operate['info']) # 'msg' ????
        return {'result':True }

    def get_text(self,operate):   #=-=
        if operate.get("find_type") == f.find_elements_by_id:
            element_info = self.Element_By(operate)[operate["index"]]

            result = element_info.get_attribute("text")
            re_reulst = re.findall(r'[a-zA-Z\d+\u4e00-\u9fa5]', result)  # 只匹配中文，大小写，字母
            return {"result": True, "text": "".join(re_reulst)}

        element_info = self.Element_By(operate)
        result =element_info.text
        # result = element_info.get_attribute("text")  #===>None

        re_reulst = re.findall(r'[a-zA-Z\d+\u4e00-\u9fa5]', result)   #===> [音,频,小,管,家]
        return {"result": True, "text": "".join(re_reulst)}
        pass
    def get_value(self,operate): #=-= ???
        if operate.get("find_type") == f.find_elements_by_id:
            element_info = self.Element_By(operate)[operate["index"]]

            result = element_info.get_attribute("value")
            re_reulst = re.findall(r'[a-zA-Z\d+\u4e00-\u9fa5]', result)  # 只匹配中文，大小写，字母
            return {"result": True, "text": "".join(re_reulst)}

        element_info = self.Element_By(operate)
        result = element_info.get_attribute("value")

        re_reulst = re.findall(r'[a-zA-Z\d+\u4e00-\u9fa5]', result)
        return {"result": True, "text": "".join(re_reulst)}
        pass
    def move_to_element(self,operate): #=-=
        ActionChains(self.wd).move_to_element(self.Element_By(operate)).perform()
        return {"result": True}
        pass

    def get_list(self ,operate):
        # 下拉框元素我只会用Xpath来拿
        print(" get_list 只用 xpth")
        if operate['find_type'] == f.find_elements_by_xpath:
            pass
        pass

    def get_object(self ,operate):
        #有的时候，我会获得元素对象，再通过他获得接下来的元素
        self.object = self.Element_By(operate)

    def get_driver(self ):
        self.object=None

    def switch_window(self ,operate ,total=0,target=-1):  #扩展装饰器 ,暂定两个页面的交互
        while True:
            if len(self.wd.window_handles) == int(operate['info']):
                self.handles=self.wd.window_handles
                break
        self.wd.switch_to.window(self.handles[-1])
        return {'result': True}

    def sleep(self,operate):
        import time
        time.sleep(operate['info'])
        return {'result':True}

    def close_window(self ,operate ):
        #能不能先切换窗口，再关之前那个窗口
        print('aaaa',self.wd.current_window_handle)
        time.sleep(10)
        self.wd.close()
        self.handles=self.wd.window_handles
        print(self.handles)
        print(self.wd.current_window_handle)
        self.wd.switch_to(self.handles[operate['info']])
        return {'result':True}
        pass

    def scroll_down(self ,operate):
        pass
    def scroll_up(self ,operate):
        pass
    def refresh(self,operate):
        time.sleep(operate['info'])
        self.wd.refresh()
        return {'result':True}

    def change_size(self ,operate):
        pass



    def is_Element(self ,operate):
                                           #取不到返回，后面的值
        return operate['find_type'] if operate['find_type'] != 'None' else None


    def Element_By(self,element_dic ):
        ''' lamda :  '''
        print(element_dic['element_info'])
        find = {            #不需要变量,因为后面不需要
            f.find_element_by_id:lambda   :self.wd.find_element_by_id(element_dic['element_info']),
            f.find_element_by_xpath: lambda  :self.wd.find_element_by_xpath(element_dic['element_info']),
            f.find_element_by_class_name: lambda  :self.wd.find_element_by_class_name(element_dic['element_info']),
            f.find_element_by_tag_name:lambda  :self.wd.find_element_by_tag_name(element_dic['element_info']),
            f.find_element_by_link_text:lambda  :self.wd.find_element_by_link_text(element_dic['element_info']),

            f.find_elements_by_id:lambda  : self.wd.find_elements_by_id(element_dic['element_info']),
            f.find_elements_by_xpath: lambda  :self.wd.find_elements_by_xpath(element_dic['element_info']),
            f.find_elements_by_class_name:lambda  : self.wd.find_elements_by_class_name(element_dic['element_info']),
            f.find_elements_by_tag_name:lambda  : self.wd.find_elements_by_tag_name(element_dic['element_info']),
            f.find_elements_by_link_text:lambda  : self.wd.find_elements_by_link_text(element_dic['element_info']),
        }

        return find[element_dic['find_type']]()

    def Element_By_object(self, element_dic):
        ''' lamda :  '''
        find = {
            f.find_element_by_id:lambda : self.object.find_element_by_id(element_dic['element_info']),
            f.find_element_by_xpath: lambda :self.object.find_element_by_xpath(element_dic['element_info']),
            f.find_element_by_class_name:lambda : self.object.find_element_by_class_name(element_dic['element_info']),
            f.find_element_by_tag_name:lambda : self.object.find_element_by_tag_name(element_dic['element_info']),
            f.find_element_by_link_text:lambda : self.object.find_element_by_link_text(element_dic['element_info']),

            f.find_elements_by_id:lambda : self.object.find_elements_by_id(element_dic['element_info']),
            f.find_elements_by_xpath:lambda : self.object.find_elements_by_xpath(element_dic['element_info']),
            f.find_elements_by_class_name:lambda : self.object.find_elements_by_class_name(element_dic['element_info']),
            f.find_elements_by_tag_name:lambda : self.object.find_elements_by_tag_name(element_dic['element_info']),
            f.find_elements_by_link_text:lambda : self.object.find_elements_by_link_text(element_dic['element_info']),
        }

        return find[element_dic['find_type']]()




