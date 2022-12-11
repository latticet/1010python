"""
子类重写父类的方法：
子类的方法和父类的方法重名，子类会覆盖父类
"""
# Person类
class Person:
    def __init__(self):
        self.name = '人'
        self.age = 18

    def run(self):
        print('人类跑')


# Student类
class Student(Person):
    def __init__(self):
        self.name = '学生'
        self.age = 16

    def run(self):
        print('学生跑')


student = Student()
print(student.name)
print(student.age)
student.run()
