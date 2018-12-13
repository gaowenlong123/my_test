from Base.Root.Interface import Interface
import os

class I_video(Interface):
    def __init__(self):
        super(I_video,self).__init__()


    def get_dir_name(self):
        return str(os.path.dirname(__file__).split('/')[-1])









if __name__ == '__main__':

    i = I_video()
    for i1 in range(10):
        i.write('21111sssssssssss我是文章1dadwaa')
    i.write('adada')

    # 写入dict
    b = {"aaaa": 111, "22": 222222}
    i.write_dict(b)
    i.end_write()