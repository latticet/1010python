# 需求：接收姓名和年龄，然后输出如下内容：
"""
姓名：xxx
年龄：xxx
"""
# 接收用户输入
'''
name = input('name:')
age = int(input('age:'))
height = float(input('height:'))
'''
# 输出要求的内容
"""
print('姓名:', name)
print('年龄:', age)
"""
# 变量和字符串结合在一起使用：变量的格式化输出
# TODO 第一种：f格式化（主要使用的方式）
"""
print(f'姓名：{name}')
print(f'年龄：{age}')
print('--' * 20)
print(f'姓名：{name}\n年龄：{age}')
"""

# TODO 第二种：%格式化
'''
# 要输出的变量先要占位符占位，然后在补充数据
# str占位符：%s
# int占位符：%d
# float占位符：%f
# 单个占位符使用
print('姓名：%s' % name)
print('年龄：%d' % age)
print('--' * 20)
# 多个占位符使用
print('姓名：%s\n年龄:%d' % (name, age))  # ()元组数据类型
print('--' * 20)

# %f格式化
print(height)
print('姓名：%s\n年龄:%d\n身高：%f' % (name, age, height))
print('--' * 20)

# %f调整格式化小数点位数
# %.nf n表示小数点位数
print('姓名：%s\n年龄:%d\n身高：%.2f' % (name, age, height))
print('==' * 20)
# %d
# 必须输出6位数字
# 填充0
num1 = int(input('数字：'))
print('数字：%d' % num1)
print('数字：%06d' % num1)
print('==' * 20)
'''

# 需求：生成一个6为的随机验证码
# 导入随机模块
import random

# 生成随机数(1到999999之间的随机整数)
# print(random.randint(1, 999999))
code = '%06d' % random.randint(1, 999999)
print(code)
print('==' * 20)


# %s, 其他数据类型也可以使用%s
name = input('name:')
age = int(input('age:'))
height = float(input('height:'))
print('姓名：%s' % name)
print('年龄：%s' % age)
print('身高：%s' % height)
