# TODO 函数返回None的情况
# 第一种：函数没有显示的写return
def fn1(a, b):
    print(a)
    print(b)


print(fn1(1, 2))
print('--' * 20)


# 第二种：return 后面什么都不写
def fn2(a, b):
    print(a)
    print(b)
    return


print(fn2(1, 2))
print('--' * 20)


# 第三种：return None
def fn3(a, b):
    print(a, b)
    return None


print(fn3(1, 2))
print('--' * 20)


# 练习
def fn4(a, b):
    print(a + b)


print(fn4(1, 2))  # 3 None
print('==' * 20)

# TODO 函数同时返回多个值
"""
说明：
1. 同时返回多个值之间用逗号分割
2. 同时返回的多个值会收集到一个元组类型中
"""


def fn5(name, age, addr):
    return name, age, addr, 1 + 2


t1 = fn5('刘杨', 18, '成都')
# print(t1)
# print(type(t1))
# 函数返回多个值，进行元组拆包
name, age, addr, num = fn5('王木鑫', 18, '成都')
print(name, age, addr, num)
