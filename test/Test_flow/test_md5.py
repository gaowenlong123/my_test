#学习一下java开发再说这个事情

import hashlib ,requests ,json
from Api_Server.Support.Base_Time import *

m = hashlib.md5()  # 创建md5对象

# str=str(data)+"media_partner"
# m.update(str.encode(encoding='UTF-8'))  # 生成加密串，其中password是要加密的字符串
# sign=m.hexdigest()  # 打印经过md5加密的字符串

request =requests.session()


data2={
	"device_id": "763b4fec726443ca",
	"os_version": "8.1.0",
	"param": {
		"platformId": "1",
		"siteId": "1",
		"subnavId": "59",
		"subnavNick": "recommend",
		"subnavType": "1"
	},
	"partner_id": "android",
	"partner_version": "8.1.2_dev",
	"request_id": "",
	"timestamp": time_Stamp(),
	"timestamp_period": "300"
}


pass1=json.dumps(data2)
pass_word=pass1+"media_partner"
print(pass_word)
m.update(pass_word.encode(encoding='UTF-8'))  # 生成加密串，其中password是要加密的字符串
sign=m.hexdigest()  # 打印经过md5加密的字符串
print(sign)

headers={
	'Content-Type':'application/json;charset=UTF-8',
	'sign':sign,
	'device': '763b4fec726443ca',

}
re =requests.post(url='http://gatewaytest36.36kr.com/api/mis/nav/home/subnav/recom?sign='+sign ,headers=headers,data=pass1)
print(re.text)


