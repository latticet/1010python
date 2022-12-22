# TODO 如何自定义异常
"""
class NameException(Exception):
    def __str__(self):
        return '异常描述信息'
"""

# TODO 如何抛出自定义异常
"""
raise NameException()
"""


# 自定义异常类
class LenException(Exception):
    def __str__(self):
        return '长度不合法...'


# 接收用户输入
username = input('用户名：')
try:
    if 6 <= len(username) <= 18:
        print('用户名合法')
    else:
        raise LenException()
except LenException as e:
    print(e)