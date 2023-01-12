import unittest
import ddt

# 测试数据
data_list = [
    {'username': 'fine1', 'password': '123456'},
    {'username': 'fine2', 'password': '123456'}
]


@ddt.ddt
class DemoTestCase(unittest.TestCase):

    @ddt.data(*data_list)
    def test_login(self, item):
        print(item)


if __name__ == '__main__':
    unittest.main(verbosity=2)
