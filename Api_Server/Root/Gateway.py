#Gateway 接口的基类  ,实现生成文件 ，记录信息 ；自动生成sign （每个子类有自己的 params)
from abc import abstractmethod,ABCMeta
import requests ,json ,hashlib ,copy
from Api_Server.Support.Base_APP import *
from Api_Server.Support.Base_Enums import Enums
from Api_Server.Base.Base_File import *
from Api_Server.Base.Base_Data import *
from Api_Server.Base.Base_pickle import *

class Gateway(metaclass=ABCMeta):
    def __init__(self):

        #====每个对象初始化的步骤======
        self.login_type = self.get_url()
        self.version = self.get_version()

        self.pass_word = "==="

        self.Cookie_path='E:\Pycharm_Git\my_test\Api_Server\Root\Cookie.pickle'

        self._md5 = hashlib.md5()

        #先检查本地的cookie
        if self.get_isLogin():
            self._Check_Cookie()


        #初始化属性
        self._privite_property()
        self._public_property()

        #生成临时记录数据的文件
        self.path_name=self.get_dir_name()
        self._mk_dir(self.path_name)
        self._mk_pickle(self.path_name)

        self._make_headers(self.login_type)


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
        if self.login_type ==Enums.test_App_url:
            self.Cookie=dict['App']
            self.Headers = self._make_headers(self.login_type ,self.Cookie)
            print("还没有写判断机制呢")
            self._check_request('', headers=self.Headers)
        elif type == Enums.App_url:
            self.Cookie = dict['']
            self.Headers = self._make_headers(self.login_type, self.Cookie)
            print("还没有写判断机制呢")
            self._check_request('', headers=self.Headers)

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
        ''' 手动登录，进行操作  ，记录Cookie 就行'''
        print("请手动登录，并进行操作，谢谢")
        if self.login_type ==Enums.test_App_url:
            self.Cookie = input("请输入Cookie")
            data = {'WEB': self.Cookie}
            writeInfo(data, self.Cookie_path)
        elif type == Enums.App_url:
            self.Cookie = input("请输入Cookie (线上)")
            data = {'WEB': self.Cookie}
            writeInfo(data, self.Cookie_path)

        return self._make_headers(self.login_type, self.Cookie)   #？？？？

    def _make_headers(self,type ,cookie=''):
        if type == Enums.test_App_url:
            self.Headers = {
                'Content-Type': 'application/json;charset=UTF-8',
            }
            return self.Headers
        elif type == Enums.App_url:
            # Token = ''
            # _list = cookie.split(';')
            # for i in _list:
            #     if 'M-XSRF-TOKEN' in i:
            #         Token = i.split('=')[1]
            # self.Headers = {
            #     'M-X-XSRF-TOKEN': Token,
            #     'Cookie': cookie
            # }
            return self.Headers






#公有方法区域
    def write(self ,data):  #在一次运行中可以持续写入文件。但是不能两次运行中累加
        write_text(data=data,path=self.log_text)

    def end_write(self ,is_clear):  #将pickle的信息全部中写入       (这里牵扯一个需求，字典是一个多层结构，现在只是一层字典的内容）
        write_text('运行中的字典信息',path=self.log_text)
        dict=self._read_pickle(is_clear=is_clear)
        for i in dict:
            temp = ''
            temp = '<<  '+ str(i) + '  :  '+str(dict[i]) + '  >>'
            write_text(data=temp,path=self.log_text)

    def write_dict(self,data):
        writeInfo(data,self.log_pickle)

    def MD5(self , body ):
        pass_word = body+self.pass_word
        self._md5.update(pass_word.encode('utf-8'))
        sign = self._md5.hexdigest()
        return sign

    def get_channelType_param(self , type):
        _data = channel_data_test.basic_data.copy()
        if type == channel_type.recom:
            _data.update(channel_data_test.recom)
        elif type == channel_type.video:
            _data.update(channel_data_test.video)
        return _data

    def get_postdata(self ,type):
        # 这个函数不能在父类调用，因为在编译的时候还不知道具体请求那个频道信息流 !!!!
        _params = self.get_channelType_param(type)

        _post_data = {
            "partner_id": "ios",
            "partner_version": self.version,
            # "device_id": "92772661-C750-433A-9024-55CB605FDFFC",
            "param": _params,
        }

        return _post_data




    #抽象方法区域
    @abstractmethod
    def get_dir_name(self):
        return ''

    @abstractmethod
    def get_isLogin(self):
        return False

    @abstractmethod
    def get_url(self):
        #在这里区分的是测试环境还是线上环境
        return ''

    @abstractmethod
    def get_version(self):
        return version.V8_0

    # @abstractmethod
    # def get_param(self):
    #     return {}






    # 公有属性区域
    # @abstractmethod
    def _public_property(self):
        pass


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
   # writeInfo({'App':'aaaaaa'},'Cookie.pickle')
