"""
工具类文件，用于对一些文件数据的读取，设置断言方法
"""

import json


# 设置通用断言方法


def assert_test(httpcode, success, code, message, response, self):
    self.assertEqual(httpcode, response.status_code)
    self.assertEqual(success, response.json().get("success"))
    self.assertEqual(code, response.json().get("code"))
    self.assertIn(message, response.json().get("message"))


# 定义一个函数，用于对部门数据json文件的读取
def get_departement_json(path,name):
    with open(path, mode="r", encoding="utf-8") as f:
        jsonData = json.load(f)
        depart_data = jsonData.get(name)
        reslut_list = list()
        reslut_list.append(tuple(depart_data.values()))
    return reslut_list
