# TODO 第一种[常用]
"""
try:
    可能发生异常的代码
except Exception as result:
    print(result)
"""
"""
try:
    num = int(input('num:'))
    result = 1 / num
except Exception as e:
    print(e)
"""

# TODO 第二种
"""
try:
    可能发生异常的代码
except:
    print(result)
"""

try:
    num = int(input('num:'))
    result = 1 / num
except:
    print('Fail')
