# 变量
name = 'module1'


# 函数
def fn():
    print('module1-fn函数执行')


# 类
class Demo:
    pass


# 指定当前模块from...import * 时，可以被导入的资源
# 注意：标识符的字符串形式
__all__ = ['name', 'fn']
