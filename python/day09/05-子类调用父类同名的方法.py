"""
super()
"""


# Person类
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print('人类工作')


# Student类
class Student(Person):
    def __init__(self, name, age, number):
        super().__init__(name, age)
        self.number = number

    def work(self):
        # 简单写法（一般就这种）
        super().work()
        # 传统写法
        # super(Student, self).work()
        print('学生写作业')


student = Student('hello', 18, 100)
print(student.name)
print(student.age)
print(student.number)

student.work()
