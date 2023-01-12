import unittest


class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('setUpClass')

    def setUp(self) -> None:
        print('setUp')

    def tearDown(self) -> None:
        print('tearDown')

    def test01(self):
        print('test01')

    def test02(self):
        print('test02')

    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDownClass')


if __name__ == '__main__':
    unittest.main(verbosity=2)
