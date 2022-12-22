# 注释
# 单行注释
# 多行注释
"""
多行注
"""

# 规范
# 语法规范   必须遵循
# 编码规范   一般建议遵循
# PEP8规范，让python程序员写出风格统一的代码、

# 变量
str1 = 'hello'
str2 = 'world'
str3 = 'hello'

# 变量常见操作
a, b, c = 1, 2, 3

a = b = c = 100

x = 100
y = 10
x, y = y, x

# 输入
"""
input('描述信息：')
"""
# 阻塞程序向下运行，接收用户输入
# 得到字符串类型

# 输出
"""
print('msg', '...', sep=' ', end='\n')
print(1, 2, 3, sep='')
"""

# python数据类型
# 不可变
"""
number: int float
str
bool
None
tuple
"""
# 可变
"""
list
dict
set
"""
# 序列
# 下标， 切片， 进行遍历
# str tuple list

# 容器数据类型
# str:
# 索引， 切片
# + * index rindex find
# join split strip rstrip replace
str1 = 'hello'
# index找不到会报错
# index 查找子字符串在字符串中的位置, 从左至右查
print(str1.index('l'))
# rindex 查找子字符串在字符串中的位置, 从右至左查
print(str1.rindex('l'))

# print(str1.index('a'))

# find找不到返回-1
print(str1.find('a'))
print(str1.rfind('a'))

# tuple
# 索引， 切片， 遍历， 拆包

# list
# 有序，不唯一
# 索引， 切片
# 方法：append insert extend index pop

# dict
# key:value
# 方法：pop keys values items

# set
# 去重唯一
# set(list)









