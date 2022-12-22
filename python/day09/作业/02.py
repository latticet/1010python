"""
新建一个文件，定义一个猫类，创建一个猫对象，调用上面的属性和方法
"""


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print(f'{self.name}在跑')

    def eat(self):
        print(f'{self.name}在吃')


cat = Cat('Tom', 5)
cat.run()
cat.eat()
