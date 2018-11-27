import unittest
from selenium import webdriver
import os
from Base.BaseYaml import getYaml
from Base.BaseLog import myLog

#将路径跳转到P文件夹中
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def get_driver():
    # chromedriver = PATH("../exe/chromedriver.exe")  #暂不添加吧
    # os.environ["webdriver.chrome.driver"] = chromedriver  #添加环境变量
    # driver = webdriver.Chrome(chromedriver)
    driver =webdriver.Chrome()
    driver.maximize_window()  # 将浏览器最大化
    openurl = getYaml(PATH("../Yamls/Config.yaml"))[1]['url']
    print(openurl)
    #有一个初始化的配置yaml，                   并且[1]是因为yaml数据又被装进一个list中
    driver.get(openurl)
    driver.implicitly_wait(10)
    return driver       #返回一个webdrier


class ParametrizedTestCase(unittest.TestCase):
    """ TestCase classes that want to be parametrized should
        inherit from this class.
    """

    def __init__(self, methodName='runTest', param=None):
        super(ParametrizedTestCase, self).__init__(methodName)
        self.param=param

    @classmethod
    def setUpClass(cls):
        print('执行测试2')
        cls.driver = get_driver()
        cls.logTest = myLog().getLog("chrome")  # 每个设备实例化一个日志记录器

    def setUp(self):
        pass

    @classmethod
    def tearDownClass(cls):
        print('结束测试3')
        import time
        time.sleep(2)
        cls.driver.close()
        cls.driver.quit()
        pass

    def tearDown(self):
        print('结束测试1')
        pass

    @staticmethod
    def parametrize(testcase_klass, param=None):
        # print("---parametrize-----")
        # 先添加测试用例，再执行
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_klass(name, param=param))
        return suite


if __name__ == '__main__':
    pass
    ##执行自动化测试脚本的方法  通过parametrize
    # suite = unittest.TestSuite()
    # suite.addTest(ParametrizedTestCase.parametrize(TestOne, param=1))
    # suite.addTest(ParametrizedTestCase.parametrize(TestOne, param=13))
    # unittest.TextTestRunner(verbosity=2).run(suite)
