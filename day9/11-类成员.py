# TODO 类属性
"""
语法：
class Demo:
    属性名 = 属性值
说明：
类属性属于整个类，包括这个类的所有实例
"""


class Person:
    # 类属性
    country = '中国'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 类的外部
# 获取类属性
# 语法：类名.类属性名
print(Person.country)
p1 = Person('hello', 18)
print(p1.country)

# 类属性修改
# 语法：类名.类属性名 = new_value
Person.country = 'China'
print(Person.country)
p1.country = 'xxx'
print(p1.country)
print(Person.country)

# 类属性删除
del Person.country
# print(Person.country)
print('==' * 20)

# TODO 类方法
"""
语法：
class Demo:
    @classmethod   装饰器
    def fn(cls):
        pass
        
调用：
类名.类方法名()   # 一般这种
对象.类方法名()
说明：
@classmethod：   装饰器
cls：当前类
"""


class Person:
    # 类属性
    country = '中国'

    # 类方法
    @classmethod
    def info(cls):
        print(cls)
        print(cls.country)



# 类方法调用
# print(Person)
Person.info()
# Person().info()
