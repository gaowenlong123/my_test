# def check(*args ,**kwargs):
    #     #*args 用来将多余参数打包成tuple给函数体调用
    #     # **kwargs 打包关键字参数成dict给函数体调用
    #     #(6,7,8,9,a=1, b=2, c=3)     ===> 输出结果  ： 6 （ 7，8,9） {'a'=1,'b'=2,'c'=3}
import functools

def asert_success(func):
    @functools.wraps(func)
    def check(data,*args ,**kwargs):
        if data["_isSuccess"] == False:
            # 如果 为false 就不执行被装饰的函数
            return data
        return func(data , *args ,**kwargs)

    return check




@asert_success
def a(dict):
    print(dict)

if __name__ == '__main__':
    a({"11":1 ,"_isSuccess":True})

