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
print('--' * 20)
str3 = 'hello'
str4 = 'hello'
print(str3 is str4)  # True

list1 = ['python', 'mysql', 100]
list2 = ['python', 'mysql', 100]
list3 = list1

print(list1 is list2)  # False
print('==' * 20)

# TODO 逻辑运算符
# 表达式：可以在一行写的代码
# 逻辑运算符使用布尔类型进行运算
# and  并且，and俩边表达式结果都为真，那么and表达式的结果为True，否则为False
print(True and True)  # True
print(False and True)  # False
print('--' * 20)
# or 或者，or俩边的表达式只要有一个是True，那么or表达式的结果就是True，否则就是False
print(True or True)  # True
print(False or True)  # True
print(False or False)  # False
print('--' * 20)

# not 取反
print(not True)  # False
print(not False)  # True
print('--' * 20)

# 短路
# 其他数据类型或者是表达式使用逻辑运算符
# 其他数据类型转化为False：0 '' None [] {} ()
# and
print(1 and 2)  # 2
print(2 and 1)  # 1
print(0 and 1)  # 0
print('hello' and '0')  # '0'
print('hello' and 0)  # 0
print('--' * 20)

# or
print(1 or 2)
print(2 or 1)
print(0 or 1)
print('hello' or '0')
print('hello' or 0)
print(0 or 1)
