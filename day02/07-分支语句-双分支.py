# 语法
"""
if 条件表达式:
    条件成立执行的代码块1
else:
    条件不成立执行的代码块2
"""
# 执行流程
"""
条件成立执行代码块1
条件不成立执行代码块2
"""

num1 = int(input('num1:'))
num2 = int(input('num2:'))

if num1 >= num2:
    print(f'num1:{num1}')
else:
    print(f'num2:{num2}')
