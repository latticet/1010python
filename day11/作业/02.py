"""
2. 定义一个函数模块
可以去除传入的字符串里面的所有空格，返回去除空格之后的字符串
"""


def del_space():
    string = input('字符串:')
    return string.replace(' ', '')


print(del_space())
