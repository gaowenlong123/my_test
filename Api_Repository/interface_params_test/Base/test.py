from Api_Server.Root_Gateway.Base_DateCenter import *
from Api_Server.Root_Gateway.Base_request import *
from Api_Server.Decorate_Data.Extract_Value_Tostring import *
from Api_Server.Decorate_Data.Extract_Dict_Value import *
from Api_Server.Support.Base_APP import *


for i in range(3):
    print(i)
    data1 = App_request(channel_data(channel_param.hot),environment=1)
    # print(data1)
    data2 = get_dict_value(data1, template_path='data/itemList')
    # keyValues_ToString(data=data2, key_list=["itemType","widgetTitle","categoryTitle","route"])
    keyValue_ToString_byIndex(data=data2, by_index=[2, 3, 4, 7],
                              key_list=["itemType", "widgetTitle", "categoryTitle", "route"])
    time.sleep(5)