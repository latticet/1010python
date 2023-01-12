import unittest


class Demo1TestCase(unittest.TestCase):
    def test01(self):
        print('test01')

    def test02(self):
        self.assertTrue(0)
