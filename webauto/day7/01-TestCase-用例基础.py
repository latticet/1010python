import unittest


class DemoTestCase(unittest.TestCase):
    def test02(self):
        print('test02')

    def test01(self):
        print('test01')


    def test03(self):
        print('test03')

    def my_test(self):
        print('mytest')


if __name__ == '__main__':
    unittest.main(verbosity=2)
