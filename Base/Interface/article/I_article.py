from Base.Root.Interface import Interface
import os


class I_article(Interface):
    def __init__(self):
        super(I_article ,self).__init__()
        pass


    #会调用，但是里面需要具体的实现方法啊
    def get_dir_name(self):
        dir_name=str(os.path.dirname(__file__).split('/')[-1])
        return dir_name
















if __name__ == '__main__':
    #例
    i=I_article()

    #写入text
    for i1 in range(10):
        i.write('21111sssssssssss我是文章1dadwaa')
    i.write('adada')

    #写入dict
    b={"aaaa":111,"22":222222}
    i.write_dict(b)
    i.end_write()

