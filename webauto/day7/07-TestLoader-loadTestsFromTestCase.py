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
    # 创建loader对象
    loader = unittest.TestLoader()
    # 加载测试用例
    # 通过类名加载测试用例, 返回suite
    suite1 = loader.loadTestsFromTestCase(Demo1TestCase)
    suite2 = loader.loadTestsFromTestCase(Demo2TestCase)

    # 创建suite
    suite = unittest.TestSuite()
    # 第一种
    """
    suite.addTest(suite1)
    suite.addTest(suite2)
    """

    # 第二种
    suite.addTests([suite1, suite2])

    # 创建执行器
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
