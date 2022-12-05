# 定义函数时的参数
# TODO 必填参数（必须参数）
# 必填参数在函数调用的时候，必须传入对应的实参
def fn1(a, b):
    print(a, b)


fn1(1, 2)
print('==' * 20)

# TODO 默认参数
# 默认参数，在函数调用的时候，可以不用传入实参。
# 不传，使用默认值
# 传入，使用自定义值
"""
说明：
默认参数必须写在必填参数的后面
"""


def add_stu(name, age, class_name='1010'):
    print(name, age, class_name)


add_stu('hello', 16)
add_stu('good', 18)
add_stu('apple', 17, '1111')
