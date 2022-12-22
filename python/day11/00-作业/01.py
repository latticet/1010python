"""
模块里面具有 三个类
厨师: 炒菜方法
服务员: 接待客人方法  送走客人方法
收银员: 收钱方法
客人来-->服务员接待-->客人点菜-->厨师炒菜-->客人吃完了-->收营员收钱-->服务员送客
"""


class A:
    def cooking(self):
        print('炒菜')


class B:
    @staticmethod
    def welcome():
        print('接待客人')

    @staticmethod
    def send():
        print('送走客人')


class C:
    def money(self):
        print('收钱')


print('客人来')
B.welcome()
print('客人点菜')
A().cooking()
