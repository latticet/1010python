"""
__new__：魔术方法
触发：创建对象时
作用：Create and return a new object
"""

"""
如果new不加*args和**kwargs
试试init里面有参数还可以使用吗
"""


class Demo(object):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)


d1 = Demo(1, 2)
print(d1)

d2 = Demo(1, 2)
print(d2)
