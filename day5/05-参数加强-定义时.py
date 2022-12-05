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
print('==' * 20)

# TODO 不定长参数(万能参数)
# 说明：没有固定的长度，可以随意传入实参
# 位置不定长
"""
def fn(*args):
    args
args说明：args是一个元组类型，收集fn函数调用时传入的所有位置参数 
"""


def fn2(*args):
    print(args)


fn2(1, )
fn2(1, 2, 'hello')
fn2(1, 2, 'hello', 'good')
print('--' * 20)
# 关键字不定长
"""
def fn(**kwargs):
    kwargs  
kwargs说明：args是一个字典类型，收集fn函数调用时传入的所有关键字参数 
"""


def fn3(**kwargs):
    print(kwargs)


fn3(a=1, b=2, c='hello')
fn3(a=1, b='python', c='mysql', d='linux')
print('==' * 20)


# 位置不定长和关键字不定长一起使用
def fn4(*args, **kwargs):
    print(args)
    print(kwargs)


fn4(1, 2, 3, a=100, b=200)
print('==' * 20)


# 使用所有参数形式
def fn5(a, b, *args, aa=11, bb=12, **kwargs):
    print(a, b)
    print(args)
    print(aa, bb)
    print(kwargs)


fn5(1, 2, 100, 200, 300, aa=110, bb=120, x='hello', y='good')
