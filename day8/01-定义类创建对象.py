# TODO 类
"""
语法：
class 类名:
    pass
类名：
    遵循标识符的命名规范
    类名一般使用大驼峰命名方式
"""


# 定义类
class Person:
    pass


# TODO 对象
# 类和对象的关系
# 先创建类，通过类创建对象
"""
语法：
类名()  
作用：
创建（实例化）了这个类的一个实例（对象）
说明：
1. 一个类可以创建多个对象
2. 对象之间是隔离的,每创建一个新的对象都会开辟一个新的内存空间来进行存储
"""
# 创建对象
p1 = Person()
# print(id(p1))
# hex:将10进制转化为16进制
# print(hex(id(p1)))
print(p1)

p2 = Person()
print(p2)

p3 = Person()
print(p3)
