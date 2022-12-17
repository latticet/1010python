"""
说明：列表推导式就是快速生成列表的一种表达式
特点：
    1. 语法更简洁
    2. 效率更高效

语法：[生成元素的表达式 控制元素生成个数的表达式]
常用方式:
变量 = [表达式 for 变量 in 列表]
"""
# 需求：1到10的一个列表
# 传统方式
"""
list1 = []
for i in range(1, 11):
    list1.append(i)

print(list1)
"""
# 列表推导式
list2 = [i for i in range(1, 11)]
print(list2)
print('==' * 20)

# 1到10之间的偶数
# 第一种
list3 = [i for i in range(2, 11, 2)]
print(list3)
print('--' * 20)
# 第二种
list4 = [i for i in range(1, 11) if i % 2 == 0]
print(list4)
print('--' * 20)
# 第三种
list4_1 = []
for i in range(1, 11):
    if i % 2 == 0:
        list4_1.append(i)

print(list4_1)
print('==' * 20)

# [(1, 1), (1, 2), (2, 1), (2, 2)]
list5 = [(i, j) for i in range(1, 3) for j in range(1, 3)]
print(list5)
print('--' * 20)

list5_1 = []
for i in range(1, 3):
    for j in range(1, 3):
        list5_1.append((i, j))

print(list5_1)
