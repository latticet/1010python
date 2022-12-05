# 定义函数
def add(a, b, c, d):
    return a + b + c + d


# 列表
list1 = [1, 2, 3, 4]
tuple1 = ('a', 'b', 'c', 'd')
print(add(list1[0], list1[1], list1[2], list1[3]))

# TODO 位置参数拆包
print(add(*list1))
print(add(*tuple1))
print('==' * 20)

# TODO 关键字参数拆包
dict1 = {
    'b': 2,
    'a': 1,
    'c': 3,
    'd': 4
}
print(add(**dict1))
