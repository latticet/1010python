import unittest


class TestCase(unittest.TestCase):
    def test01(self):
        # assertEqual(a, b [,msg=断言失败描述信息] ) 断言a和b相等
        # assertEqual(预期，实际)
        self.assertEqual('hello', 'hello')
        # self.assertEqual('hello', '你好')

    def test02(self):
        self.assertTrue('hello')
        self.assertTrue(0)



if __name__ == '__main__':
    unittest.main(verbosity=2)