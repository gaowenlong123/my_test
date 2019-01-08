import requests ,json
from Api_Server.Support.Base_Compare import *

class I_yellowPage():
    def __init__(self ,param=''):
        self.url = "http://gatewaytest36.36kr.com/api/mrs"
        # self.url = "http://gateway.36kr.com/api/mrs"
        self.request=requests.session()

    def project_list(self ,num=10 ):
        _url =self.url +"/project/catalogue"

        headers = {}
        headers['Content-Type'] = 'application/json;charset=UTF-8'
        data={
            "partner_id":"web",
            "param":{
            "pageEvent":0,
            "pageSize":num
            }
        }
        re=self.request.post(url=_url ,data=json.dumps(data) ,headers=headers)
        try:
            temp = re.json()['data']['projectList'][:num]

        except:
            temp={}
        _list=[]

        for dict in temp:
            s1=map(dict,'name',"无")
            s2=map(dict , 'briefIntro' ,"无")
            s3=map(dict , 'reportStatus',"无")
            s4 = map(dict, 'trade', "无")
            s5 = map(dict, 'financingRound', "无")
            # _list.append(s1+"简介:"+s2 + " financingRound: " +s3)
            print(s1+ "   简介:"+s2 +"    trade:" +s4[0]+"    Round:"+ s5 +"    reportStatus:" +s3 )
        # print("资讯==>",_list)


    def project_homepage(self ,url='' ,articleSize=0 ,teamSize=1):
        _url =self.url +"/project/homepage"

        headers = {}
        headers['Content-Type'] = 'application/json;charset=UTF-8'
        data={
            "partner_id":"web",
            "param":{
            "identityName" :url,
            "articleSize":articleSize,
            "teamMemberSize":teamSize
            }
        }
        re=self.request.post(url=_url ,data=json.dumps(data) ,headers=headers)
        print(re.text)

    def relate_article(self ,url=''):
        #相关报道文章 ， 项目管理文章才会有
        _url = self.url + "/project/article"

        headers = {}
        headers['Content-Type'] = 'application/json;charset=UTF-8'
        data = {
            "partner_id": "web",
            "param": {
                "identityName": url,
                "pageSize": 1,
                "pageEvent": 0
            }
        }
        re = self.request.post(url=_url, data=json.dumps(data), headers=headers)
        # print(re.text)
        try:
            temp = re.json()['data']['articleList']

        except:
            temp={}
        _list=[]

        for dict in temp:
            s1=map(dict,'id',"无")
            s2=map(dict , 'title' ,"无")
            s3=map(dict , 'publishTime',"无")
            # _list.append(s1+"简介:"+s2 + " financingRound: " +s3)
            print(s2 +"   id:"+str(s1) +"   publishTime: " +s3 )

    def project_team(self ,url=''):
        _url =self.url +"/project/team"

        headers = {}
        headers['Content-Type'] = 'application/json;charset=UTF-8'
        data={
            "partner_id":"web",
            "param":{
            "identityName" :url,
            "pageSize":5,
            "pageEvent":0
            }
        }
        re=self.request.post(url=_url ,data=json.dumps(data) ,headers=headers)
        print(re.text)
        try:
            temp = re.json()['data']['teamMemberList']

        except:
            temp={}
        _list=[]

        for dict in temp:
            s1=map(dict,'name',"无")
            s2=map(dict , 'jobTitle' ,"无")
            s3=map(dict , 'description',"无")
            # _list.append(s1+"简介:"+s2 + " financingRound: " +s3)
            print(s1 +"   jobTitle:"+s2 +"   description: " +s3 )


    def article_mention(self):

        _url = self.url + "/project/mention"
        headers = {}
        headers['Content-Type'] = 'application/json;charset=UTF-8'
        data = {
            "partner_id": "web",
            "param": {
                "​articleId": 10465629
            }
        }
        re = self.request.post(url=_url, data=json.dumps(data), headers=headers)
        print(re.text)
if __name__ == '__main__':
    i = I_yellowPage()
    # i.project_list()
    i.project_homepage(url="project1545994744" ,articleSize=0 ,teamSize=10)
    # i.relate_article(url="dididache")
    # i.project_team(url="project1545980816")

    # i.article_mention()  # 有问题