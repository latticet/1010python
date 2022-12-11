"""
多继承：一个类同时继承多个父类
"""


class A:
    def info_a(self):
        print('a')


class B:
    def info_b(self):
        print('b')


# C类继承了A类和B类
class C(A, B):
    pass


c = C()
c.info_a()
c.info_b()
