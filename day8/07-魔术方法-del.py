"""
__del__
说明：析构函数
触发：当对象被销毁时，触发del方法的执行
作用：对象销毁之前的收尾工作
"""


class Demo:
    def __del__(self):
        print('del执行了')


d1 = Demo()

# 删除
# del d1


# 封装一个文件操作的类
