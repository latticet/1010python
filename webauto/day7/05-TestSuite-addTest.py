# TestSuite收集要执行的测试用例
# addTest() 收集单个测试用例
import unittest


class Demo1TestCase(unittest.TestCase):
    def test01(self):
        print('test01')

    def test02(self):
        print('test02')


class Demo2TestCase(unittest.TestCase):
    def test_a(self):
        print('test_a')

    def test_b(self):
        print('test_2')


if __name__ == '__main__':
    # 创建TestSuite对象
    suite = unittest.TestSuite()
    # 收集测试用例
    suite.addTest(Demo2TestCase('test_a'))
    suite.addTest(Demo1TestCase('test01'))

    # 创建TestRunner对象
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
