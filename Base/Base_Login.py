import requests

header = {
    # "origin": "http://test01web.36kr.com",
    "Referer": "http://test01web.36kr.com/",
    # 'User-Agent': 'userAgent',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}

post_data={"client_id":6,
      "country_code":"86",
      "account":"23322332233",
      "password":"er2222",
      "type":"login"}

r_login = requests.post('https://accounttest12.36kr.com/api/v1/sign-in',data=post_data ,headers=header)
print(r_login.text)


