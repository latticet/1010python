"""
语法：
try:
    可能发生异常的代码
except 异常的类型:
    捕获到异常执行的代码
"""
# 捕获成功
try:
    result = 1 / 0
except ZeroDivisionError:
    print('0不能作为除数使用')

# 捕获不成功
# try:
#     result = 1 / 0
# except NameError:
#     print('0不能作为除数使用')

# 没有异常
try:
    result = 0 / 1
except NameError:
    print('ok')

print(1111)
