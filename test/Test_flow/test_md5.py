#学习一下java开发再说这个事情

import hashlib ,requests ,json ,base64
from Api_Server.Support.Base_Time import *

m = hashlib.md5()  # 创建md5对象

# str=str(data)+"media_partner"
# m.update(str.encode(encoding='UTF-8'))  # 生成加密串，其中password是要加密的字符串
# sign=m.hexdigest()  # 打印经过md5加密的字符串

request =requests.session()


data2={
	"device_id": "763b4fec726443ca",
	# "os_version": "8.1.0",
	"param": {
		"platformId": "1",
		"siteId": "1",
		"subnavId": "59",
		"subnavNick": "recommend",
		"subnavType": "1"
	},
	"partner_id": "android",
	"partner_version": "8.1.2_dev",
	# "request_id": "",
	# "timestamp": time_Stamp(),
	# "timestamp_period": "300"
}

data3={

	# "os_version": "8.1.0",
	"partner_id": "ios",
	"partner_version": "8.1",
	# "device_id": "92772661-C750-433A-9024-55CB605FDFFC",
	"param": {
		"subnavType": "1",
		"homeCallback": "",
        "siteId": "1",
		"subnavId": "59",
		"platformId": "1",
		"subnavNick": "recommend",
	},

	# "request_id": "",
	# "timestamp":1546513175456,
	# "timestamp":time_Stamp(),
	# "timestamp_period": "300"

}

data4={

	# "os_version": "8.1.0",
	# "partner_id": "android",
	"partner_id": "ios",
	"partner_version": "8.1",
	# "device_id": "92772661-C750-433A-9024-55CB605FDFFC",
	"param": {
		"subnavType": "1",
		"homeCallback": "",
        "siteId": "1",
		"subnavId": "59",
		"platformId": "1",
		"subnavNick": "recommend",
	}

	# "request_id": "",
	# "timestamp":1546513175456,
	# # "timestamp":time_Stamp(),
	# "timestamp_period": "300"

}


pass1=json.dumps(data3)
pass_word=pass1+ "ystDqsMYEeep0Ov0FW3AWQ"
# print(type(pass1))
# print(type(pass_word.encode('utf-8') ))
# print(pass_word.encode('utf-8'))
# print(base64.b64encode( pass_word.encode('utf-8')))
m.update( pass_word.encode('utf-8'))  # 生成加密串，其中password是要加密的字符串
sign=m.hexdigest()  # 打印经过md5加密的字符串
print(sign)

headers={
	'Content-Type':'application/json;charset=UTF-8',
	# 'sign':sign,
    # "Cookie":"Accept=application/json;Accept=application/json;kr_pinyou_device_uuid.sig=RJuDqU0Eqa8tRM3MEA6EkI1QOyBxs5smolbvqpznxWw;kr_device_id.sig=cYBjZoiCfBRPtdjptgbvrXuWRWFtPqxnhMDp8Kbemoc;kr_device_id=763b4fec726443ca;krnewsfrontss=fd60e65068c6b63db38c6c43e4c83c78;acw_tc="";kr_pinyou_device_uuid=869720035244865",
	# 'device': '763b4fec726443ca',

}
re =requests.post(url='http://gatewaytest36.36kr.com/api/mis/nav/home/subnav/recom?sign='+sign ,headers=headers,data=json.dumps(data4))
print(re.text)


