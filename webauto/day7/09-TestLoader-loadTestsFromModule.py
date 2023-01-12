from unittest import defaultTestLoader, TestSuite, TextTestRunner
from case import demo1_testcase, demo2_testcase

# loader.loadTestsFromModule()    通过测试模块

# 创建loader对象
# loader = unittest.TestLoader()
suite1 = defaultTestLoader.loadTestsFromModule(demo1_testcase)
suite2 = defaultTestLoader.loadTestsFromModule(demo2_testcase)

# suite
suite = TestSuite()
suite.addTests([suite1, suite2])

# runner
runner = TextTestRunner()
runner.run(suite)
