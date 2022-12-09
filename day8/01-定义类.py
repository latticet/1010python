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


# 类和对象的关系
# 先创建类，通过类创建对象
"""
语法：
类名()  
说明：
创建（实例化）了这个类的一个实例（对象）
一个类创建多个对象,对象之间是隔离的。
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
