"""
多态实现
1. 子类继承父类
2. 子类重写父类的方法
3. 调用这个方法
"""


# 动物类
class Animal:
    def call(self):
        print('动物叫')


# 狗类
class Dog(Animal):
    def call(self):
        print('旺旺旺')


# 猫类
class Cat(Animal):
    def call(self):
        print('喵喵喵')


# 人类
class Person():
    pass


# 调用
# cat = Cat()
# dog = Dog()


# cat.call()
# dog.call()


def do_call(obj):
    # 开始时间
    obj.call()
    # 结束时间
    # 结束时间 - 开始时间


do_call(Cat())
do_call(Dog())
do_call(Person())
