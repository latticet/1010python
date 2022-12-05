# 函数调用时
# 定义函数
def fn1(a, b):
    print(f'a:{a}, b:{b}')
    return a + b


# TODO 位置传参（位置参数）
# 按形参的顺序传入实参
print(fn1(100, 200))
print('==' * 20)

# TODO 关键字传参（关键字参数）
# 按形参的名字传入实参
print(fn1(b='100', a='200'))
print('--' * 20)
print(fn1(a='hello ', b='world'))
print('==' * 20)

# 关键字和位置一起使用
print(fn1('hello', b=' world'))
