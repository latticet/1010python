import unittest
from HTMLTestRunner import HTMLTestRunner
import os
import time

# 加载要执行的测试用例
suite = unittest.defaultTestLoader.discover('case', '*_testcase.py')

# 准备测试报告文件路径
report_path = os.path.abspath('report')
file_path = os.path.join(report_path, time.strftime('%Y%m%d%H%M%S') + '-测试报告.html')

with open(file_path, 'wb') as f:
    # 创建执行器对象
    runner = HTMLTestRunner(
        title='测试报告标题',
        description='测试描述',
        tester='张三|李四|王五',
        stream=f,
    )
    # 执行测试用例
    runner.run(suite)


from selenium import webdriver

driver = webdriver.Chrome()
driver.switch_to.frame()
