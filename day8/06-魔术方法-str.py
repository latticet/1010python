"""
__str__:
说明：对象字符串输出方式
触发: 当对象用print打印的时候，str魔术方法执行
作用：输出对象的关键信息
注意：str必须返回字符串类型
"""


# 定义类
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


# 创建对象
p1 = Person('hello')
print(p1)

p2 = Person('good')
print(p2)
