header={
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
# 'Content-Type': 'application/json',
'Referer': 'http://test01web.36kr.com/',
}


'''
Cookie: krnewsfrontss=f104f00e59640e800d088c4e33219312; 
        M-XSRF-TOKEN=3d56345df145762c60303df28f19217d3de8ddd54dfb723d70e90e17c5f96b0e; 
        Hm_lvt_713123c60a0e86982326bae1a51083e1=1543579250; 
        Hm_lvt_1684191ccae0314c6254306a8333d090=1543579250; 
        kr_stat_uuid=CkEKd25726320; 
        sajssdk_2015_cross_new_user=1; 
        sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22CkEKd25726320%22%2C%22%24device_id%22%3A%22167647e2c629e-0cafacb0d5c6ee-333b5602-1049088-167647e2c6457a%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22167647e2c629e-0cafacb0d5c6ee-333b5602-1049088-167647e2c6457a%22%7D; 
        Hm_lpvt_1684191ccae0314c6254306a8333d090=1543579253; 
        Hm_lpvt_713123c60a0e86982326bae1a51083e1=1543579253; 
        new_user_guidance=true
'''

from Test_flow.test2 import get
token=get()
cokies='M-XSRF-TOKEN='+token
header['Cookie']=cokies
import json
post_data={"client_id":6,"country_code":"86","account":"23322228888","password":"er2222","type":"login"}

import requests
kr=requests.session()
a=kr.post('https://accounttest12.36kr.com/api/v1/sign-in' ,data=post_data ,headers=header)
print(a.text)


url='https://36kr.com/pp/api/like'
header1 = {
    # "origin": "http://test01web.36kr.com",
    "Referer": "http://test01web.36kr.com/p/10464803",
    'Access-Control-Request-Headers': 'm-x-xsrf-toke',
    'M-X-XSRF-TOKEN':token,
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}
header1['']=cokies
post_data1={"ltype":"post","lid":10464803,"direction":"plus"}

r=kr.post(url=url,data=post_data,headers=header1)
print(r.text)