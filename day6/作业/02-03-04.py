"""
1. 封装函数,实现返回三个数的和
2. 封装函数,实现返回三个数的最大值
3. 封装函数,实现返回三个数的最小值
"""


def fn1(a, b, c):
    return a + b + c


def fn2(a, b, c):
    return max([a, b, c])


def fn3(a, b, c):
    return min([a, b, c])


print(fn1(1, 2, 3))
print(fn2(1, 2, 3))
print(fn3(1, 2, 3))
