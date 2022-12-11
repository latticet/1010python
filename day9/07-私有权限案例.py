class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def set_age(self, age):
        if 1 <= age < 120:
            self.__age = age
        else:
            print('年龄不合理')

    def get_age(self):
        return self.__age


p1 = Person('hello', 18)

# 修改年龄
p1.set_age(30)
print(p1.get_age())
