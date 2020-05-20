"""
封装接口的基本设置，如url，传入参数等，用于执行文件的调用
"""

# 创建一个类，
import requests


class DepartmentApi:
    # 实例化url
    def __init__(self):
        self.ihrm_url = "http://ihrm-test.itheima.net/api/sys/login"
        self.depart_url = "http://ihrm-test.itheima.net/api/company/department/"

    # 登录ihrm系统
    def login_ihrm(self, json):
        headers = {"Content-Type": "application/json"}
        return requests.post(url=self.ihrm_url, json=json, headers=headers)

    # 添加部门模块
    def add_department(self, headers, name, code, manager, introduce, ):
        json = {"name": name, "code": code, "manager": manager, "introduce": introduce}
        return requests.post(url=self.depart_url, headers=headers, json=json)

    # 查看添加的部门
    def check_department(self, headers, id):
        return requests.get(url=self.depart_url + "/" + id, headers=headers)

    # 修改部门的信息
    def put_department(self, headers, id, json):
        return requests.put(url=self.depart_url + "/" + id, json=json, headers=headers)

    # 删除部门
    def delete_department(self, headers, id):
        return requests.delete(url=self.depart_url + "/" + id, headers=headers)
