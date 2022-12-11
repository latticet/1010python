"""
python中没有严格的受保护权限
语法：_成员名
特点：只能在类的内部和派生类中访问
"""


class Person:
    def __init__(self):
        self._name = 'hello'


print(Person()._name)
