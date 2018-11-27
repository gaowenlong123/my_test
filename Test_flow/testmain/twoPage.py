from Base.BaseRunner import ParametrizedTestCase
import os
import sys
from ZZZtest.testPage.twoPage import TwoPage
from Base.BaseOs import change_path


class two(ParametrizedTestCase):
    def testALoginFail(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": change_path("../Yamls/Content_Management/mytest.yaml"),
               "caseName": sys._getframe().f_code.co_name}

        page = TwoPage(app)
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
        super(two, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(two, cls).tearDownClass()
