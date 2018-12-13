# 地方站
import os , time ,requests
from Base.Support.Base_Enums import Enums
from Base.Root.Interface import Interface

class I_local(Interface):
    def __init__(self,param = ''):
        super(I_local ,self).__init__()

        self.request=requests.session()


    def get_dir_name(self):
        '''
          #必须重新，获得该文件夹名，生成存储文件
        :return: dir_name
        '''
        dir_name=str(os.path.dirname(__file__).split('/')[-1])
        return dir_name

    def get_post_Data(self , para):
        '''
        得到输入的参数，拼接生成可以发送请求的文章参数
        :return: 可以提交的文章的结构体
        '''
        pass

    def get_url(self):
        return Enums.test_Web_url

    def _public_property(self):
        pass





if __name__ == '__main__':
    i = I_local()
#







