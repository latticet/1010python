"""
私有成员：具有私有权限的属性和方法
成员：属性和方法
私有属性：在属性名前加__,就是私有属性
私有方法：在方法名前加__,就是私有方法
私有权限：只能在类的内部访问
"""


class Person:
    def __init__(self, name, age):
        self.__name = name  # 私有属性
        self.age = age

    # 私有方法
    def __info(self):
        print('info')

    def test(self):
        print(self.__name)


class Student(Person):
    def get_father(self):
        print(self.age)
        print(self.__name)


# p1 = Person('hello', 18)
# p1.test()

# print(p1.age)
# TODO 类的外部访问私有属性
# print(p1.__name)
# p1.__info()

# TODO 派生类中访问私有属性
s1 = Student('hello', 19)
s1.get_father()
