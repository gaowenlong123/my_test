from Base.Root.Interface import Interface
import os


class I_article(Interface):
    def __init__(self ,para=''):
        super(I_article ,self).__init__()

        #文件新建文章需要的自定义的数据
        self.article_Data=self.get_post_Data(para)

        #得到文章ID
        # self.ID = self.get_ID()




  #重写虚方法
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


    #文章类的基本属性  （1:自己定义的标题、图片等，可以随时改变， 2：系统提供的属性，创建时间等等，不可直接更改的（1：不能更改的 2：可以通过系统事件来更改的）那么就是只读吧


    #文章的基本方法
    def get_dict(self):
        '''
        将得到的对象，转成字典
        :return: dict
        '''
        pass


    #文章类拥有的接口
    def recommend(self ,id):
        '''
            url : http://cmstest02.36kr.com/api/post/10464983/recommend
           str : {"recommend_info":"{\"feed_ids\":[269]}"}
           json: recommend_info={"feed_ids":[269]}

           :return {"code":0}
           :type    put
           request
Host: cmstest02.36kr.com
Connection: keep-alive
Content-Length: 41
Accept: */*
Origin: http://cmstest02.36kr.com
x-requested-with: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36
Content-Type: application/json
Referer: http://cmstest02.36kr.com/posts
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: .....
       '''

    def get_ID(self):
        '''
        在编辑页面的提交文章标题时，会生成文章ID
        :return:  文章的ID
        '''
        pass









if __name__ == '__main__':
    #例
    i=I_article()

    #写入text
    for i1 in range(10):
        i.write('21111sssssssssss我是文章1dadwaa')
    i.write('adada')

    #写入dict
    b={"aaaa":111,"22":222222}
    c={'dada':222444}
    i.write_dict(b)
    i.write_dict(c)
    i.end_write(is_clear=False)   #将存的字典写入text中 ,不删除文件

    print(i.Headers)





