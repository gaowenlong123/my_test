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
        self.Cookie_path='E:\Pycharm_Git\my_test\Base\Root\Cookie.pickle'

        #建立一个seesion  ? 要不要直接建立一个seesion 到处用
        # self.request=requests.session()

        #先检查本地的cookie
        self._Check_Cookie()


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
            raise("还没有写判断机制呢")
            self._check_request('', self.Headers)

    def _check_request(self , url,headers):
        '''  检查请求结果 '''
        re=requests.get(url=url ,headers=headers)
        if re.json()['code'] == 0:
            print(re.text)
            print('Cookie  没有过期')
        else:
            # 重新启动
            print('Cookie  过期')
            self._Restart_driver()

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

        return self._make_headers(self.login_type, self.Cookie)

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

    def _get_Cookie(self):
        return self._driver.get_Cookie()

    def _get_Token(self):
        return self._driver.get_Token()




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








    #抽象方法区域
    @abstractmethod
    def get_dir_name(self):
        return ''







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
   a=read_pickle('Cookie.pickle')
   print(a)




