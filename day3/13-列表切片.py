"""
切片作用：
一次性获取多个元素
切片语法：
list[start:end:step]
start:开始下标，默认为0
end:结束下标，不包括结束位置
step:步长，默认为。
    正数：从左至右进行切片
    负数：从右至左进行切片
切片说明：
1. 切片之后，返回一个新的列表
2. start,end,step都可以为负数
"""

list1 = ['python', 'mysql', 'linux', 'shell', 'git']
# TODO 正数
# python, mysql
print(list1[0:2:1])
print(list1[:2])
print('==' * 20)

# python, linux, git
print(list1[0:5:2])
print(list1[0::2])
print('==' * 20)

# TODO 负数
# python, mysql
print(list1[-5:-3])
print(list1[-5:-3:1])

# python, linux, git
print(list1[-5::2])
print('==' * 20)

list2 = ['a', 'b', 'c', 'd', 'e', 'f']
print(list2[-2:-5:1])  # []  整数：从左至右
print(list2[-2:-5:-1])  # [e, d, c] 负数：从右至左

print(list2[5:2:-1])
print('==' * 20)

# 切片拷贝， 拷贝一份一摸一样的数据
list3 = list2[:]
list4 = list2
