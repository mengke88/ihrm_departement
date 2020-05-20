"""
执行测试用例的文件
"""
# 1.导包
import logging
import unittest

from parameterized import parameterized

import app
from api.department_api import DepartmentApi
from utils import assert_test, get_departement_json


class IHRMDepart(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.depart_api = DepartmentApi()

    # 登录数据
    def test_01_login(self):
        json = {"mobile": "13800000002", "password": "123456"}
        response = self.depart_api.login_ihrm(json)
        # 断言
        logging.info("返回数据为：{}".format(response.json()))
        print("输入数据为：", json)
        assert_test(200, True, 10000, "操作成功", response, self)
        # 获取令牌
        token = response.json().get("data")
        # 通过全局变量来获取token，要导入app文件
        app.Headers = {"Content-Type": "application/json", "Authorization": token}

    # 添加部门，利用参数化
    @parameterized.expand(get_departement_json("../data/dapaetment_data", "add_depart"))
    def test_02_add_department(self, name, code, manager, introduce, httpcode, success, code1, message):
        print("name={},code={},manager={},introduce={}".format(name, code, manager, introduce))
        response_add = self.depart_api.add_department(app.Headers, name, code, manager, introduce)
        # 打印日志
        logging.info("返回数据为：{}".format(response_add.json()))
        print("添加部门返回的数据：", response_add.json())
        # 断言
        assert_test(httpcode, success, code1, message, response_add, self)
        # 通过全局变量获取添加员工的id，这样进行下面的操作才可以通过id进行访问
        app.depat_id = response_add.json().get("data").get("id")

    # 查看添加的部门,实现参数化
    @parameterized.expand(get_departement_json("../data/dapaetment_data", "check_depart"))
    def test_03_check_department(self, httpcode, success, code1, message):
        response_check = self.depart_api.check_department(app.Headers, app.depat_id)
        # 打印日志
        logging.info("返回数据为：{}".format(response_check.json()))
        print("添加的员工信息为：", response_check.json())
        # 断言
        assert_test(httpcode, success, code1, message, response_check, self)

    # 修改部门
    @parameterized.expand(get_departement_json("../data/dapaetment_data", "put_depart"))
    def test_04_put_department(self, name, code, manager, introduce, httpcode, success, code1, message):
        # 修改的数据
        json = {"name": name, "code": code, "manager": manager, "introduce": introduce}
        response_put = self.depart_api.put_department(app.Headers, app.depat_id, json)
        # 打印日志
        logging.info("返回数据为：{}".format(response_put.json()))
        print("修改的数据为：", json)
        print("修改返回数据", response_put.json())

        # 断言
        assert_test(httpcode, success, code1, message, response_put, self)

    # 删除部门
    @parameterized.expand(get_departement_json("../data/dapaetment_data", "delete_depart"))
    def test_05_delete_department(self, httpcode, success, code1, message):
        response_del = self.depart_api.delete_department(app.Headers, app.depat_id)
        # 打印日志
        logging.info("返回数据为：{}".format(response_del.json()))
        print("删除模块返回数据：", response_del.json())
        # 断言
        assert_test(httpcode, success, code1, message, response_del, self)
