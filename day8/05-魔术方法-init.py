"""
__init__:
说明：对象初始化方法
触发: 创建对象以后触发init方法的执行
作用：初始化对象属性
"""


# 定义类
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_name(self, name):
        self.name = name

# 创建对象
p1 = Person('aa', 11)
print(p1.name)
print(p1.age)

p1.set_name('aaaa')
print(p1.name)

p2 = Person('bb', 22)
print(p2.name)
print(p2.age)
