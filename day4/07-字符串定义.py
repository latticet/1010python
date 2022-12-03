# 1
str1 = 'hello'
# 2
str2 = "hello"
# 3
str3 = '''hello'''
# 4
str4 = """hello"""

print(str1, str2, str3, str4)
print(type(str1))
print(type(str2))
print(type(str3))
print(type(str4))
print('==' * 20)

# 四种方式的区别：
"""
1. 单引号和双引号没有区别
2. 三单引号和三双引号没有区别
3. 三引号字符串的格式会被输出到终端
"""


str5 = 'hello     ' \
       'world'
print(str5)
print('--' * 20)
str6 = """
你好
世界
"""
print(str6)

# 说明
# 不可变数据类型


# 小结
# 可变数据类型
"""
list
"""
# 不可变数据类型
"""
str
tuple
number
bool
"""


