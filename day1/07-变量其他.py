# TODO 多个值赋值给多个变量
a, b, c = 1, 2, 3

# TODO 多个变量赋值相同的值
x = y = 100

# TODO 交换变量的值
m = 100
n = 200

# 第一种：传统方式
t = m
m = n
n = t

print(m, n)

# 第二种：简单方式
m, n = n, m
print(m, n)
