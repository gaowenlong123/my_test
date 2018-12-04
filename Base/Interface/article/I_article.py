from Base.Root.Interface import Interface
import os


class I_article(Interface):
    def __init__(self ,para=''):
        super(I_article ,self).__init__()

        print('dddd')
        #文件新建文章需要的自定义的数据
        # self.ID = self.get_ID()
        # self.article_data=self.get_Data(para)



    #必须重新，获得该文件夹名，生成存储文件
    def get_dir_name(self):
        dir_name=str(os.path.dirname(__file__).split('/')[-1])
        return dir_name


    #文章类的基本属性  （标题，图片，等等


    #文章类拥有的方法  （

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

    def get_Data(self , para):
        '''
        得到输入的参数，拼接生成可以请求的参数
        :return: 可以提交的数据的体
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
    i.end_write()   #将存的字典写入text中

    print(i.Headers)





