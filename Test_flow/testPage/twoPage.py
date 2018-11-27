from Base import BaseRunPage
from Base.BaseYaml import getYaml


class TwoPage:
    def __init__(self, kwargs):
        _init = {"driver": kwargs["driver"], "test_msg": getYaml(kwargs["path"]),
                 "logTest": kwargs["logTest"], "caseName": kwargs["caseName"]}
        self.page = BaseRunPage.PagesObjects(_init)

    def operate(self):  # 操作步骤
        self.page.operate()

    def checkPoint(self):  # 检查点
        self.page.checkPoint()
