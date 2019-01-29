#接口的基类  ,实现生成文件 ，记录信息 ；得到COokie
from abc import abstractmethod,ABCMeta
import requests
from Api_Server.Base.Base_Driver import WebDriver
from Api_Server.Support.Base_Enums import Enums
from Api_Server.Base.Base_File import *
from Api_Server.Base.Base_Text import *
from Api_Server.Base.Base_pickle import *

class Interface(metaclass=ABCMeta):
    def __init__(self):

        #====每个对象初始化的步骤======
        self.login_type = self.get_url()
        self.Cookie_path=Enums.cookie_path

        # self.request=requests.session()

        #先检查本地的cookie
        self._Check_Cookie()

        #初始化属性
        self._privite_property()
        self._public_property()

        #生成临时记录数据的文件
        self.path_name=self.get_dir_name()
        # self._mk_dir(self.path_name)
        # self._mk_pickle(self.path_name)



#私有方法区域
    def _mk_dir(self ,name=''):
        '''
        创建记录文件，并初始化
        '''
        if ":" in name:
            name +="\\"+ name.split('\\')[-1]
        self.log_text=name+'.txt'
        mkdir_file(self.log_text)
        write_text_init(self.log_text)

    def _mk_pickle(self ,name=''):
        if ":" in name:
            name += "\\" + name.split('\\')[-1]
        self.log_pickle = name + '.pickle'
        mkdir_file(self.log_pickle)
        write_pickle_init(data={},path=self.log_pickle)

    def _read_pickle(self ,is_clear):
        return read_pickle(self.log_pickle ,is_clear=is_clear)

    def _Check_Cookie(self):
        dict = read_pickle(self.Cookie_path)
        if self.login_type ==Enums.test_Cms_url:
            self.Cookie=dict['CMS']
            self.Headers = self._make_headers(self.login_type ,self.Cookie)
            self._check_request('http://cmstest02.36kr.com/api/post?per_page=1&page=1', headers=self.Headers)

        elif self.login_type == Enums.test_Web_url:
            Token=''
            self.Cookie = dict['WEB']
            _list = self.Cookie.split(';')
            for i in _list:
                if 'M-XSRF-TOKEN' in i:
                    Token = i.split('=')[1]
            self.Headers = self._make_headers(self.login_type, self.Cookie)
            print("还没有写判断机制呢")
            # self._check_request('', self.Headers)

        elif self.login_type==Enums.test_Mrs_url:
            self.Cookie = dict['MRS']
            self.Headers = self._make_headers(self.login_type, self.Cookie)
            self._check_request('http://mrstest43.corp.36kr.com/api/organ/organization/list?param.pageSize=10&param.pageNo=1', headers=self.Headers)

    def _check_request(self , url,headers):
        '''  检查请求结果 '''
        re=requests.get(url=url ,headers=headers)
        if '502' in re.text:
            print("502")
            assert "环境问题"
        try:
            if re.json()['code'] == 0:

                print(re,' In Interface.py')
                print('Cookie  没有过期')
            else:
                # 重新启动
                print('Cookie  过期')
                self._Restart_driver()
        except:
            print('出错了')
            # self._Restart_driver()

    def _Restart_driver(self):
        ''' Cookie写入文件  ， 返回Headers 就行'''
        # 重启浏览器  ,
        self._driver = WebDriver()
        self._driver.login(self.login_type)

        if self.login_type == Enums.test_Web_url:
            self.Cookie = self._get_Cookie()
            data={'WEB':self.Cookie}
            writeInfo(data ,self.Cookie_path)
        elif self.login_type == Enums.test_Cms_url:
            self.Cookie = self._get_Cookie()
            data = {'CMS': self.Cookie}
            writeInfo( data ,self.Cookie_path)

        elif self.login_type == Enums.test_Mrs_url:
            self.Cookie = self._get_Cookie()
            data = {'MRS':self.Cookie}
            writeInfo(data , self.Cookie_path)

        self._close_window()
        return self._make_headers(self.login_type, self.Cookie)

    def _close_window(self):
        pass

    def _make_headers(self,type ,cookie):
        if type == Enums.test_Cms_url:
            self.Headers = {
                'x-requested-with': 'XMLHttpRequest',
                'Cookie': cookie,
            }
            return self.Headers
        elif type == Enums.test_Web_url:
            Token = ''
            _list = cookie.split(';')
            for i in _list:
                if 'M-XSRF-TOKEN' in i:
                    Token = i.split('=')[1]
            self.Headers = {
                'M-X-XSRF-TOKEN': Token,
                'Cookie': cookie
            }
            return self.Headers
        elif type == Enums.test_Mrs_url:
            self.Headers = {
                'Content-Type': 'application/json;charset=UTF-8',
                'Cookie': cookie,
            }

            return self.Headers


    def _get_Cookie(self):
        return self._driver.get_Cookie()

    def _get_Token(self):
        return self._driver.get_Token()




#公有方法区域
    def write(self ,data):
        write_text(data=data,path=self.log_text)

    def end_write(self ,is_clear):
        write_text('运行中的字典信息',path=self.log_text)
        dict=self._read_pickle(is_clear=is_clear)
        for i in dict:
            temp = ''
            temp = '<<  '+ str(i) + '  :  '+str(dict[i]) + '  >>'
            write_text(data=temp,path=self.log_text)

    def write_dict(self,data):
        writeInfo(data,self.log_pickle)




    #抽象方法区域
    @abstractmethod
    def get_dir_name(self):
        return ''

    @abstractmethod
    def get_post_Data(self , para):
        return {}

    @abstractmethod
    def get_url(self):
        return ''

    # 公有属性区域
    @abstractmethod
    def _public_property(self):
        self.request_data = {}
        self.response_data = {}




#私有属性区域,只读不能写
    def _privite_property(self):
        self._auther = ''
        self._error_times = 0
        self._error_frequency = []


    @property
    def auther(self):
        return self._auther

    @property
    def Error_Times(self):
        return self._error_times

    @property
    def Error_Frequency(self):
        return self._error_frequency








if __name__ == '__main__':
   a=read_pickle('Cookie.pickle')
   print(a)
   # writeInfo({'MRS':'aaaaaa'},'Cookie.pickle')



