#接口的基类  ,实现生成文件 ，记录信息 ；得到COokie
from abc import abstractmethod,ABCMeta
import os ,requests
from Base.Support.Base_Driver import WebDriver
from Base.Support.Base_Enums import Enums
from Base.Base.Base_File import *
from Base.Base.Base_Data import *
from Base.Base.Base_pickle import *

class Interface(metaclass=ABCMeta):
    def __init__(self):

        #====每个对象初始化的步骤======
        self.login_type = Enums.test_Cms_url

        #建立一个seesion
        # self.request=requests.session()

        #先检查本地的cookie           如果是cms，就不需要token
        self._Check_Cookie()

        # 如果没有运行，保持diriver ，如果有就跳过
        # self._driver = WebDriver()
        # self._driver.login(self.login_type)

        #初始化属性
        self._privite_property()
        self._public_property()

        #生成临时记录数据的文件
        self.path_name=self.get_dir_name()
        self._mk_dir(self.path_name)
        self._mk_pickle(self.path_name)





#公有属性区域
    def _public_property(self):
        self.request_data = {}
        self.response_data = {}

        # 这个搞成全局的先试试 ,一次拿到全局都用

        self.Headers=self._get_Headers()




#私有方法区域
    def _mk_dir(self ,name=''):
        '''
        创建记录文件，并初始化
        '''
        self.log_text=name+'.text'
        mkdir_file(self.log_text)
        write_text_init(self.log_text)

    def _mk_pickle(self ,name=''):
        self.log_pickle = name+'.pickle'
        mkdir_file(self.log_pickle)
        write_pickle_init(data={},path=self.log_pickle)

    def _read_pickle(self):
        return read_pickle(self.log_pickle ,is_clear=True)

    def _Check_Cookie(self):
        mkdir_file('Cookie.text')
        temp = read_text('Cookie.text').split('\n')
        if self.login_type ==Enums.test_Cms_url:
            self.Cookie=temp[0].split(':')[1]
            self.Headers = {
                'x-requested-with': 'XMLHttpRequest',
                'Cookie': self.Cookie,
            }

            self._check_request('http://cmstest02.36kr.com/api/post?per_page=1&page=1', headers=self.Headers)

        elif self.login_type == Enums.test_Web_url:
            self.Cookie = temp[1].split(':')[1]
            _list = self.Cookie.split(';')
            for i in _list:
                if 'M-XSRF-TOKEN' in i:
                    self.Token = i.split('=')[1]
            self.Headers = {
                'M-X-XSRF-TOKEN': self.Token,
                'Cookie': self.Cookie
            }
            self._check_request('', self.Headers)



    def _check_request(self , url,headers):
        re=requests.get(url=url ,headers=headers)
        print(re.json()['code'])

    def _get_Cookie(self):
        # self.Cookie = self._drivr.get_Cookie()
        # return self.Cookie
        return self._driver.get_Cookie()

    def _get_Token(self):
        # self.Token = self.drivr.get_Token()
        # return self.Token
        return self._driver.get_Token()

    def _get_Headers_Token(self):
        # self.Heades_Token = self._drivr.get_headers_Token()
        # return self.Heades_Token
        return self._driver.get_headers_Token()

    def _get_Headers(self):
        return self._driver.get_headers()


#公有方法区域
    def write(self ,data):  #在一次运行中可以持续写入文件。但是不能两次运行中累加
        write_text(data=data,path=self.log_text)

    def end_write(self):  #将pickle的信息全部中写入       (这里牵扯一个需求，字典是一个多层结构，现在只是一层字典的内容）
        write_text('运行中的字典信息',path=self.log_text)
        dict=self._read_pickle()
        for i in dict:
            temp = ''
            temp = '<<  '+ str(i) + '  :  '+str(dict[i]) + '  >>'
            write_text(data=temp,path=self.log_text)

    def write_dict(self,data):
        writeInfo(data,self.log_pickle)

    def Restart_driver(self):
        # 重启浏览器
        self._driver.restart()

        #改变全局header
        self.Headers_Token=self._get_Headers_Token()
        pass






    #抽象方法区域
    # @abstractmethod
    # def get_dir_name(self):
    #     return ''







#私有属性区域,只读不能写
    def _privite_property(self):
        self._auther = 'gao'
        self._FixBody = []
        self._error_times = 0
        self._error_frequency = []
        self._error_reason = []

        self._type = ''   #?????


    @property
    def auther(self):
        return self._auther

    @property
    def FixBody(self):
        return self._FixBody

    @property
    def Error_Times(self):
        return self._error_times

    @property
    def Error_Frequency(self):
        return self._error_frequency

    @property
    def Error_Reason(self):
        return self._error_reason

    @property
    def Type(self):
        return self._type






if __name__ == '__main__':
    s=Interface()
