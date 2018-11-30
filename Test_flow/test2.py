import http.cookiejar as cookielib
import requests ,sys,io



def one():
    import json
    # session代表某一次连接
    kr_Session = requests.session()
    # 因为原始的session.cookies 没有save()方法，所以需要用到cookielib中的方法LWPCookieJar，这个类实例化的cookie对象，就可以直接调用save方法。
    # kr_Session.cookies = cookielib.LWPCookieJar(filename="kr_Cookies.txt")
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
    print('====',kr_Session.cookies.get_dict())

    #https://accounttest12.36kr.com/api/v1/oauth/authorize?client_id=6&redirect_uri=https%3A%2F%2Ftest02.36kr.com%2Fpp%2Fauth%2Fsignin-callback&scope=user-info&response_type=code
    payload = {'client_id': '6',
               'redirect_uri':'https://test02.36kr.com/pp/auth/signin-callback',
               'scope':'user-info',
               'response_type':'code'
               }
    r1 =kr_Session.get("https://accounttest12.36kr.com/api/v1/oauth/authorize", params=payload)
    print(r1.url)
    print(r1)


def get():  #自动化登录完成，记录cokie值
    from selenium import webdriver
    w=webdriver.Chrome()
    w.get('http://test01web.36kr.com/')
    a=w.get_cookie('M-XSRF-TOKEN')
    print(a['value'])
    print(w.get_cookie('kr_stat_uuid'))
    print(w.get_cookie('download_animation'))
    print(w.get_cookie('device-uid'))
    print(w.get_cookie('new_user_guidance'))
    print(w.get_cookie('web_feed_id'))
    print(w.get_cookie('gr_user_id'))
    print(w.get_cookie('kr_plus_project_id'))
    print(w.get_cookie(''))
    print(w.get_cookie(''))
    print(w.get_cookie(''))
    return a['value']

get()