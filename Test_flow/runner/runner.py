#测试过程的 主入口
import sys
import unittest
sys.path.append("..")

from Base.BaseRunner import ParametrizedTestCase
from datetime import datetime

# from Base.BaseInit import mk_file
# from selenium_master.Base.BaseStatistics import countDate, writeExcel

#测试用例
from ZZZtest.testmain.one  import one
from ZZZtest.testmain.twoPage import two
# from TestCase.CnblogsTest import CnblogsTest
# from TestCase.HomeTest import HomeTest


# 可以写成手动选的，通过gui，来选择要执行的脚本，当然可执行的脚本可以生成，都可以实现的
def runnerCaseApp():
    start_time = datetime.now()
    suite = unittest.TestSuite()
    # suite.addTest(ParametrizedTestCase.parametrize(one))

    suite.addTest(ParametrizedTestCase.parametrize(two))
    # suite.addTest(ParametrizedTestCase.parametrize(MyTest))
    # suite.addTest(ParametrizedTestCase.parametrize(CnblogsTest))
    unittest.TextTestRunner(verbosity=1).run(suite)

    end_time = datetime.now()
    print('结束测试end')

    # countDate(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), str((end_time - start_time).seconds) + "秒")


if __name__ == '__main__':
    # mk_file()
    runnerCaseApp()
    # writeExcel()
