# range函数配合for循环实现具体的循环次数
# 语法：range(start, stop, step)
# 作用：生成一个可迭代的序列
# start:序列开始值，默认是0
# stop:序列结束值，不包括结束值
# step:步长,默认是1

# range(1, 5)  # [1, 2, 3, 4]
# range(5)  # [0, 1, 2, 3, 4]
# range(0, 5, 2)  # [0, 2, 4]

# 输出1-5
for i in range(1, 6):
    print(i)

# 输出5个hello world
for i in range(5):
    print('hello world')