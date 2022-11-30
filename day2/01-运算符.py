# TODO 算术运算符
# % 取模|取余
print(10 % 3)
print(10 % 2)
print('==' * 20)

# ** 幂运算
print(2 ** 2)
print(2 ** 3)
print(2 ** 4)
print('==' * 20)

# // 整除
print(10 // 2)
print(10 // 3)
print('==' * 20)

# / 除运算符
print(10 / 2)
print(10 / 3)
print('==' * 20)

# TODO 比较运算符
# ==
print(1 == 1)
print(1 == 2)
print('--' * 20)

# !=
print(1 != 1)
print(1 != 2)
print('==' * 20)

# TODO 赋值运算符
# +=
# 语法： a += b  a = a + b
a = 1
b = 2
a += b  # a = a + b
print(a)
print('--' * 20)

# **=
a **= 2  # a = a ** 2
print(a)
print('--' * 20)

# /=
a /= 3  # a = a / 3
print(a)
print('--' * 20)

# //=
b //= 2  # b = b // 2
print(b)
print('==' * 20)

# TODO 身份运算符
# is  a is b 判断a和b是同一个内存地址，如果是结果为True， 否则为False
str1 = 'hello'
str2 = str1
num1 = 100
num2 = 200
print(str1 is str2)
print(num1 is num2)
# is not  a is not b  判断a和b不是同一个内存地址，如果不是结果为True， 否则为False
print(str1 is not str2)
print(num1 is not num2)