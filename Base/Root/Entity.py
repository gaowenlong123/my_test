from Base.Root.Kr_Object import Kr_Object_interface


#内容实体的基类
class Entity():
    def __init__(self):
        pass



    #实体的类都有上线下线
    #个别实体可以进行推荐  ，个别实体可以被评论
    #实体还有已发布，待发布，未发布 ，前者初始化的时候要提供 id  ， 后者要传入一些可以发布的参数才可以实例化