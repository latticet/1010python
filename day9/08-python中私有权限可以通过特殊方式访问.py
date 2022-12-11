class Person:
    def __init__(self):
        self.__name = 'hello'

    def __info(self):
        print('info')


# 通过特殊的方式，可以在类的外部访问私有成员
# 语法：_类名__成员名
p1 = Person()
print(p1._Person__name)
p1._Person__info()