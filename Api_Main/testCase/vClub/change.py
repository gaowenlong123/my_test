from Api_Repository.Interface.MRS.vClub.I_vClub import I_vClub
import time


i=I_vClub()
data={"name":"测试11",
        "hasSold":"1",
        "identityName":"shige",
        "briefIntro":"简介",
        "focusDomain":"关注领域",
        "intro":"详细介绍",
        "capitalScale":"资金规模",
        "closeup":"12344",
        "keywords":"关键字,资本",
        "orgUserId":"1234567",
        "officialWebsite":"http://1111",
        "wechatQrcode":"",
        "weibo":"http://11111",
        "investmentCaseList":[{"name":"0","briefIntro":"0","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA94fa28b4b5f845b4bf6783e110258d28","displayOrder":1},{"name":"1","briefIntro":"1","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA666b34334e214dbe991e91001e4757be","displayOrder":2},{"name":"2","briefIntro":"2","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA79c7ae6f33f6419791601f401fa5a1f9","displayOrder":3},{"name":"3","briefIntro":"3","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA3823d8cbf6d1450cbf097b83ad6f5dd5","displayOrder":4},{"name":"4","briefIntro":"4","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA6cc30c98b6ec4bcb9d796e16e1e48c08","displayOrder":5},{"name":"5","briefIntro":"5","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA62c0b981c5d34060a01d4bd600e83d37","displayOrder":6},{"name":"6","briefIntro":"6","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA52e47b7144494b74a830d12e4592a1c8","displayOrder":7},{"name":"7","briefIntro":"7","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA4a8a079b912848a1a00f60e9bbd936b5","displayOrder":8},{"name":"8","briefIntro":"8","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA73670c3a07ce4259800cbacb1c4aec47","displayOrder":9},{"name":"9","briefIntro":"9","logo":"/v1/20181206/YfPuR3I-qGKsl3V5g1nfMA11e2f7d8a0574cccb4ab1e8f618ded0a","displayOrder":10}],
        "logoUrl":"/v1/20181206/iGy_0sHpe1B0H9btvRumYQ6a2fedb92f5843258e8e179f2bd6257c",}

def test1(id):
    i.mod({'name':'测试修改状态'},id ,is_sold=False)
    time.sleep(10)
    i.mod({'name':'测试修改状态22'} ,id,is_sold=True)

def test2(link=''):
    '''测试重复标题'''
    data['name']='test'+time.strftime('%M.%S', time.localtime(time.time()))
    data["identityName"]=link
    i.add(data,is_sold=True)
    time.sleep(3)
    data['name'] = 'test' + time.strftime('%M.%S', time.localtime(time.time()))
    i.add(data,is_sold=True)

def test3(id=48):
    '''测试修改'''
    i.mod({"name":'bukaixin111'},id,is_sold=False)
    pass

def test4(id):
    i.mod(data,id,is_sold=True)


if __name__ == '__main__':
    # test2('ccc')
    # test3(163)
    test4(150)
    # i.add(data,is_sold=True)
    # i.get_mod_init(158)