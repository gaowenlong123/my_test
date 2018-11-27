from Base.BaseRunner import ParametrizedTestCase
import os
import sys
from ZZZtest.testPage.onepage import LoginPage
# from ZZZtest.testPage.onepage import LoginFailPage
from Base.BaseOs import change_path




class one(ParametrizedTestCase):
    def testALoginFail(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": change_path("../Yamls/Content_Management/test.yaml"),
               "caseName": sys._getframe().f_code.co_name}

        page = LoginPage(app)
        page.operate()
        page.checkPoint()

    # def testBLogin(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../Yamls/home/Login.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #
    #     page = LoginPage(app)
    #     page.operate()
    #     page.checkPoint()

    @classmethod
    def setUpClass(cls):
        # 登录
        print('执行测试1')
        super(one, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        #一个test结束运行
        print('结束测试2')
        super(one, cls).tearDownClass()
