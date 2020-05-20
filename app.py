"""
配置环境的文件，可用于生成日志，设置全局变量
"""
# 导入logging包
import logging.handlers
import os

# 设置全局变量，用于函数与函数之间属性的调用
import time

Headers = None
depat_id = None


# 生成日志
def get_department_log():
    # 创建日志对象，设置日志级别
    logger = logging.getLogger()
    logger.setLevel(level=logging.INFO)
    # 创建输出到控制台
    ls = logging.StreamHandler()
    # 创建输出到文件中，并设置当前执行文件目录地址
    filename = os.path.dirname(os.path.abspath(__file__)) + "/log/test.log"
    path = logging.handlers.TimedRotatingFileHandler(filename=filename,when="midnight",interval=5,
                                                     backupCount=2,encoding="utf-8")
    # 创建格式化器，设置输出什么什么内容，以什么格式进行输出
    formatter = logging.Formatter(fmt="%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s")
    # 给处理器添加我们上面创建格式化形式输出
    ls.setFormatter(formatter)
    path.setFormatter(formatter)
    # 给日志添加上面设置好的处理器
    logger.addHandler(ls)
    logger.addHandler(path)

