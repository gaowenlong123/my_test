class a():
    def __init__(self):
        pass

    def say(self):
        print('a')



class b():
    def __init__(self):
        self.a=a()



from selenium import webdriver

# e=webdriver.Chrome()
# e.get('http://cmstest02.36kr.com')
# cok =e.get_cookies()
# print(cok)
# cookie=''
# for i in cok:
#     print(i[ 'name'] ,'  ====  ',end=' ')
#     print(i['value'])
#     cookie +=i['name']+'='+i['value']+';'
#
# print(cookie[:-1])
headers={
    'x-requested-with': 'XMLHttpRequest',
    'Cookie': 'kr_plus_id=12186523;kr_stat_uuid=3TT4Z25731883;download_animation=1;krnewscmscc=eyJpdiI6IkRcL2h0WjJhS2FxYWs3T3dwOHVONzlnPT0iLCJ2YWx1ZSI6InFQZFo4XC9XczgwN0dBTVNSR3hWRlZDZUFocmQ0OE1pbkNzUVJ4YlJHM095bGlYeng4Mll1cHVZUDN3YXRKblBuYXlDOTJoSzZJZVZGYUZEQWF2OStEcjlKMlNJZENTZmhhMG04Skp5XC9UQ1pMMXJXSlwvNTlpRnVuTHFzWkdLZVwveXNTU3FZbDQ0OCttd3dZXC9OcUhVTGdqY2tNVVwvSWVUVDhVRFk0R1RicDdzOTJtOUhkdXJxb0Y1SGtWZlBoV1hJYUVsR0VRelpCVXJOUjk1M29yZnU4c05TQmJwQVEwT0lxaHhDNUFaWXVyVlRTM3QxZWs4T04ySUVLc2ZwUnEzSnZTR3pwVGVWdElSY01QelFtdEhLWFNhUTIwQ2lhSzRHcjVMQTdyc09wSzhLd2RzZlAzSnh0THcyN3hjcFlpSmI2ZldOZDVQUENVV0NQSGRzVE1qMTVNQT09IiwibWFjIjoiYzQwNjE4Mjc0MzUzNTQwZGUyZTY3MGFkZDk5OTM3YWEzNWU5N2JhMDE3OGI0OTE2Njc3YWRlODRjOTE5NjFjZCJ9;krnewscmsss=eyJpdiI6ImR4YmpwRllYV1RSQjM1UGNoUU10T3c9PSIsInZhbHVlIjoiTDNIXC9zTlZjUW5XN0NQb3FTT0hnQ21TckswM3NLUlFhZWRHZXhsZFdWbkxZTzZ1eGtJMjB4bTBxeUY1eTFIWEJLSW43akx0WTJvV3hENFRVOCt1ZFFBPT0iLCJtYWMiOiIwZWM4NTJiYmQyODkzMmQ2OGVmNDcxOTVkYmI1YTA3YzVlZjZkOWVhNmNiNTM0N2M3YjkwZGY3MDRiOTE4ZmRjIn0%3D;kr_plus_project_id=1'}

import requests

# {
# 'x-requested-with': 'XMLHttpRequest',
# 'Cookie': 1,
# }
import json
post={"recommend_info":"{\"feed_ids\":[269,59]}"}
# {"recommend_info":"{\"feed_ids\":[295,59,106]}"}
b1=requests.put('http://cmstest02.36kr.com/api/post/10464761/recommend',headers=headers,data=post)
print(b1.text)


c=requests.get('http://cmstest02.36kr.com/api/post?per_page=1&page=1',headers=headers)
print(c.text)

#17:28 , 可以运行
#第二天   13：01