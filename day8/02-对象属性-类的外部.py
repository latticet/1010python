# 定义类
class Person:
    pass


# 创建对象
p1 = Person()

# TODO 设置属性
# 语法：obj.属性名 = value
p1.name = '蒋望舒'
p1.age = 18

# TODO 查看属性
# 语法：obj.属性名
print(p1.name)
print(p1.age)

# TODO 修改属性
# 语法：obj.属性名 = new_value
p1.name = '毛佳'
p1.age = 19
print(p1.name)
print(p1.age)

# TODO 删除属性
# del obj.属性名
del p1.name
print(p1.age)
print(p1.name)

