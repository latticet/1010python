# 定义装饰器
def wrapper(fn):
    def inner(a, b):
        print('正在计算中...')
        fn(a, b)

    return inner


# 求2个数的和
@wrapper
def total(num1, num2):
    print(num1 + num2)


total(1, 2)
