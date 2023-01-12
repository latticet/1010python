import unittest

# loader.loadTestsFromName(str)       通过测试模块名|类名|方法名加载
# 创建loader
loader = unittest.TestLoader()

# TODO 通过测试模块名加载
# suite = loader.loadTestsFromName('case.demo1_testcase')

# TODO 通过类名加载
# suite = loader.loadTestsFromName('case.demo2_testcase.Demo2TestCase')
# suite = loader.loadTestsFromName('demo3_testcase.Demo3TestCase')

# TODO 通过方法名加载
# suite = loader.loadTestsFromName('case.demo2_testcase.Demo2TestCase.test_a')


# loader.loadTestsFromNames(str)       批量通过测试模块名|类名|方法名加载
method_list = [
    'case.demo2_testcase.Demo2TestCase.test_a',
    'case.demo1_testcase.Demo1TestCase.test01',
    'case.demo2_testcase.Demo2TestCase.test_b'
]
suite = loader.loadTestsFromNames(method_list)

# 创建runner
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
