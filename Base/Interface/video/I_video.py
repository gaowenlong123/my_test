from Base.Root.Interface import Interface
import os

class I_video(Interface):
    def __init__(self):
        super(I_video,self).__init__()


    def get_dir_name(self):
        return str(os.path.dirname(__file__).split('/')[-1])


i = I_video()
for ia in range(5):
    i.end_write('dadada')