# 分支语句
# 单分支
# 双分支
# 多分支

# 语法
"""
if 条件表达式:
    代码块
"""
# 执行流程
"""
1. if条件表达式执行的结果只有True或者False
2. 如果if后的条件为True，那么就执行代码块
3. 如果if后的条件为False，那么就不执行代码块
"""
if 2 > 1:
    print('2大于1')

if 1 > 2:
    print('1大于2')

if 1:
    print('ok')
print('==' * 20)

num1 = int(input('num1:'))
num2 = int(input('num2:'))

if num1 > num2:
    print('num1大于num2')
