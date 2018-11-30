# app 往服务器传输 是不是有协议问题
# sign 签名验证

'''
签名字符串（待签名字符串）：按照自己设定的规则生成，我这里是把所有参数 用key=value&key=value....的形式组合起来作为签名字符串
时间戳： 主要目的就是标识请求发起的时间，可以用yyyyMMddHHmmssfff的时间格式，也可以用long类型的时间格式，这个看自己怎么规划
appid： 用于标识应用信息，给调用接口的客户端(app，企业，或者其他服务商)生成唯一的appid，这里的应用可以是某个企业，某个app，某个客户，等等，就像你去调用微信公众号的接口时，微信公众号会给你分配一个appId和appsecret
token：用于标识用户信息，区别于appid，一个是标识某个用户的信息，一个是应用的信息，用户每次登陆，生成一个用户token，用户的每次操作，通过token作为票据交换数据，token具有有效期，过期之后需要重新登陆
'''

import requests

# 1
# r = requests.get('http://test01web.36kr.com/')
# print(r.text)  #html
# print(r.url)     #url
# print(r.request)  #请求的类型
# print(r.content)  #以字节的方式去显示
# print(r.encoding)   #网页编码
# print(r.status_code)  #状态码
# print(r.history)     查看他的跳转
# print(r.headers)       #来获取响应头内容
# print(r.request.headers) #获得请求头
#自定义请求头部
# headers = {'User-Agent': 'alexkh'}
# r = requests.get('http://www.zhidaow.com', headers = headers)


#拼接链接
# payload = {'wd': '张亚楠'}
# r1 = requests.get("http://www.baidu.com/s", params=payload)
# print(r1.url)                  # http://www.baidu.com/s?wd=%E5%BC%A0%E4%BA%9A%E6%A5%A0



# 登录

# r_login = requests.post(url=url,data=post_data ,headers=header)
# print(r_login.text)

'''
在上一步，我们已经成功登录到网站了。那么接下来要如何访问站点中其他页面呢。
前面提到过，网站是通过cookie和session来标记是哪个用户访问的。
所以，在我们登录成功之后，有很重要的一步，就是我们需要把cookie保存下来，下一次请求这个站点的页面时，把这个cookie带过去。
'''

#保留cookie
def session_Login():

    import http.cookiejar as cookielib
    import json
    # session代表某一次连接
    kr_Session = requests.session()
    # 因为原始的session.cookies 没有save()方法，所以需要用到cookielib中的方法LWPCookieJar，这个类实例化的cookie对象，就可以直接调用save方法。
    kr_Session.cookies = cookielib.LWPCookieJar(filename="kr_Cookies.txt")
    # 登录发请求


    print("开始模拟登录")
    url = 'https://accounttest12.36kr.com/api/v1/sign-in'
    header = {
        "origin": "http://test01web.36kr.com",
        "Referer": "http://test01web.36kr.com/",
        # 'User-Agent': 'userAgent',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }

    post_data = {"client_id": 6,
                 "country_code": "86",
                 "account": "23322228888",
                 "password": "er2222",
                 "type": "login"}
    # 使用session直接post请求
    responseRes = kr_Session.post(url=url, data = post_data, headers = header )
    # 无论是否登录成功，状态码一般都是 statusCode = 200
    print(f"statusCode = {responseRes.status_code}")
    print(f"text = {responseRes.text}")
    print('====',kr_Session.cookies)



   #生产token csfr
    cs_url = 'https://test02.36kr.com/pp/auth/signin-callback?code=def50200630cfaf892eb9df630144b49db106db9b7292f6f233fcd49be8925ba0ec1425e5e28221630b8820509e369b566661cf26d430dc9d0b274403366cc3d33812093620f667cc38f4dde7d95cabb5f50a296090a4360f1be89526113c66eee526894abcbe0bc902c9f707eab9f8eee375a0f34cec87d533a1bc7e2050faf77dd9e41c8898668af308c7cfdd294fcb88036aa15bbe9d452b87b147bb7e3e892b0756fa35636f62b10ab5e650248ce7c2ba7ed037a41efd220fdaabca8b2f41cdb6b033914307dc3de7ef558fcfff2e091d1844be20e86acbb5db66aa35cfbb618546f8d730c8ccfc5ec561e96bcbf9c5d387684712e933b2827cada2e249837fe566924ca640ef9baed14db0d2883f486d8da9ef3fe94668c65c7d40f473120da5320369c3f4b827528fd9de39a388b9dd64352f91d122b182412385b3f4d67ab6b20de75c486a255d2542357a70790bad4215e837e0e78b73359318f38d8e92e1c60983e5e49c6292e12ee4baf73f84000eb5e0e3d13d65a06c2f55fd6c84a7d8d4348'
    cs_header = {
        "origin": "http://test01web.36kr.com",
        "Referer": "http://test01web.36kr.com/",
        # 'User-Agent': 'userAgent',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }

    # 使用session直接post请求
    responseRes = kr_Session.post(url=cs_url, headers=cs_header)
    # 无论是否登录成功，状态码一般都是 statusCode = 200
    print(f"statusCode = {responseRes.status_code}")
    print(f"text = {responseRes.text}")
    print('====', kr_Session.cookies)




    # -------------------------------------
    url1 = 'https://test02.36kr.com/pp/api/user-current'
    header1 = {
        # "origin": "http://test01web.36kr.com",
        "Referer": "http://test01web.36kr.com/",
        'Accept': 'application/json',
        # 'User-Agent': 'userAgent',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    # post_data1 = {"ltype": "post", "lid": 10464803, "direction": "plus"}
    a=kr_Session.get(url=url1,headers=header1)
    print('====', kr_Session.cookies)


    print(a.json())

    kr_Session.cookies.save()

    # return kr_Session


session_Login()


# 2
# print(r.cookies)

# r2 = requests.get('http://cmstest02.36kr.com/api/motif?per_page=100&page=1')
# print(r2.json())
# r.json()['data']['country']

