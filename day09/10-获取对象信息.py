# TODO type 查看对象类型
print(type('abc'))


class Demo:
    def info(self):
        pass


class Demo2:
    def info(self):
        pass


d1 = Demo()
print(type(d1))
print('==' * 20)

# TODO dir 查看对象的所有成员
print(dir(d1))
print(dir('hello'))
print(dir([]))
print('==' * 20)

# TODO isinstance(obj, class) 判断对象是某个类的实例
print(isinstance(d1, Demo))
print(isinstance(d1, Demo2))
print(isinstance('hello', Demo2))
print(isinstance('hello', str))
print(isinstance([], str))
print(isinstance([], list))
