# 父类
class Staff:
    def __init__(self):
        self.name = 'hello'
        self.age = 18

    def eat(self):
        print(f'{self.name}吃东西')


# 子类
class Teacher(Staff):
    pass


teacher = Teacher()
print(teacher.name)
print(teacher.age)
teacher.eat()
