# 函数说明文档 函数注释（函数的标准注释方式）
"""
语法：
def fn():
    '''
    函数的注释内容
    '''
"""


# 求2个数的和
def add(a, b):
    """
    求2个数的和    # 函数功能描述
    :param a: int 数字1
    :param b: int 数字2
    :return: int
    """
    return a + b


# 查看函数说明文档函数
help(add)

help(print)
help(len)
