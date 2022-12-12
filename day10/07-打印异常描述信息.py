"""
try:
    可能发生异常的代码
except (异常的类型1, 异常类型2, ...) as 变量名:
    发生异常执行的代码
    print(变量名)
"""

try:
    num = int(input('数字：'))
    result = 1 / num
except (ZeroDivisionError, ValueError) as e:
    print(e)
