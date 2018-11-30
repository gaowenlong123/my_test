import requests
from Test_flow.test import session_Login

url='https://36kr.com/pp/api/like'
header = {
    # "origin": "http://test01web.36kr.com",
    "Referer": "http://test01web.36kr.com/p/10464803",
    # 'User-Agent': 'userAgent',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}

post_data={"ltype":"post","lid":10464803,"direction":"plus"}

session=session_Login()
session.cookies.load()


# 去往普通页面，No
# url2='http://test01web.36kr.com/usercenter/account-password'
url2='http://test01web.36kr.com/usercenter/favorite'
r=session.get(url=url2)
print(r.request.header)

# 去往token 页面
# r=session.post(url=url,data=post_data)



# print(r.text)
