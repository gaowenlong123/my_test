#接口的基类
from abc import abstractmethod,ABCMeta
import os
from Base.Base.Base_File import *
from Base.Base.Base_Data import *

class Interface(metaclass=ABCMeta):
    def __init__(self):
        self._auther='gao'
        self._FixBody=[]
        self._error_times=0
        self._error_frequency=[]
        self._error_reason=[]

        self._request_type='post'

        self.request_data={}
        self.response_data={}

        self.mk_dir(self.get_dir_name())

    #创建记录文件，并初始化
    def _mk_dir(self ,name=''):
        self.log_text=name+'.text'
        mkdir_file(self.log_text)
        write_init(self.log_text)

    def _mk_pickle(self ):
        self.pickle=""

    def end_write(self ,data):
        write(data=data,path=self.log_text)

    def write_pickle(self):
        pass
    def _read_pickle(self):
        pass


    @abstractmethod
    def get_dir_name(self):
        return ''

    def test(self):
        print('test')








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






