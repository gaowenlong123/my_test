#接口的基类
from abc import abstractmethod,ABCMeta
import os
from Base.Base.Base_File import *
from Base.Base.Base_Data import *
from Base.Base.Base_pickle import *

class Interface(metaclass=ABCMeta):
    def __init__(self):
        #====每个对象初始化的步骤======

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

        self._request_type = ''   #?????

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
    def RequestType(self):
        return self._request_type








