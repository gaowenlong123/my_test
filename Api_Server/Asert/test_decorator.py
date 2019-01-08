#-----------
#1
# def test(func):
#     func()
#     print("aa")
#
# def one():
#     print("one" )
#
# #调用  ， 还需要调用装饰的类，能调被装饰的类后，直接执行装饰类最好
# test(one)


#2
# def test(func):
#     def say():
#         func()
#         print("aa")
#         return func()        会有返回值
#     return say()            #会自动执行
#     return say
#
# @test
# def one():
#     print("one" )
#
# #基本实现上面的需求，但是还是希望对参数进行操作
# one()


# #3
# def test(func):
#     def say(name1):
#         #可以对装饰类的参数进行修改
#         if name1 ==1:
#             name1+=1
#         func(name1)
#         print("aa")
#     return say
#

# @test
# def one(name):
#     print("one" ,name)
#
# one(1)



# 4   目标函数带不固定参数的装饰器
# def test(func):
#     def wrapper(*args ,**kwargs):
#
#         func(*args ,**kwargs)
#
#     return wrapper
#
#
# @test
# def one(name):
#     print("one" ,name)
# @test
# def one1(user,name):
#     print("one1" ,user ,name)
#
# one(1)
# one1(1,2)



#5   让装饰器带参数  目标函数每次调用重复执行指定的次数
# def decorator(max):
#     def _decorator(func):
#         def wrapper(*args ,**kwargs):
#             for i in  range(max):
#                 func(*args ,**kwargs)
#         return wrapper
#     return _decorator
#
# @decorator(3)
# def one(name):
#     print("one" ,name)
# print(one.__name__)



#5   运行时，所在的环境有误
import functools
def decorator(max):
    def _decorator(func):
        @functools.wraps(func)
        def wrapper(*args ,**kwargs):
            for i in  range(max):
                func(*args ,**kwargs)
        return wrapper
    return _decorator

@decorator(3)
def one(name):
    print("one" ,name)
print(one.__name__)


#6  装饰器类        方法可以作为装饰器，类也可以
import functools
class decorator(object):
    def __init__(self ,max):
        self.max =max
        self.count =0
    # def __call__(self, *args, **kwargs):
    def __call__(self, func):        #  对象其实也可以像函数一样调用, 只要在类的方法中实现__call__方法
        self.func = func
        return self.call_func

    # @functools.wraps(call_func)
    def call_func(self , *args, **kwargs):
        if self.max == self.count:
            print("循环测试到了")
        elif self.max > self.count:
            self.func( *args, **kwargs)
            self.count+=1
            return self.call_func(*args, **kwargs)
        else:
            pass

@decorator(10)
def say(name):
    print("test" , name)

say('aaa')


print(say.__name__)        # ????  运行环境怎么解决