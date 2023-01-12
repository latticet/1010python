import unittest

gender = input('性别：')


class TestCase(unittest.TestCase):
    @unittest.skip(reason='跳过该方法')
    def test01(self):
        print('test01')

    @unittest.skipIf(gender=='男', reason='男生跳过该用例')
    def test02(self):
        print('test02')

    @unittest.skipUnless(gender=='男', reason='女生跳过该用例')
    def test03(self):
        print('test03')

    @unittest.expectedFailure
    def test04(self):
        self.assertTrue(0)


if __name__ == '__main__':
    unittest.main(verbosity=2)

