# 定义类
"""
对象方法：
1. 对象方法在类的的内部定义
2. 必须要有一个self的参数
3. 其他和函数都相同
"""


class Person:
    # TODO 对象方法定义
    def eat(self):
        print(f'self:{self}')
        print(self.name)
        print('吃东西')

    def info(self, age, addr):
        self.age = age
        self.addr = addr


# TODO 对象方法调用
p1 = Person()
p1.name = 'hello'
print(f'p1:{p1}')
# 语法：obj.方法名()
p1.eat()
print('--' * 20)

p1.info(18, '成都')
print(p1.age)
print(p1.addr)

"""
p2 = Person()
print(f'p2:{p2}')
p2.eat()
"""
# TODO self
# self：指向调用这个方法的当前对象
# self不需要手动传入，python解释器会自动把当前调用方法的对象传入
