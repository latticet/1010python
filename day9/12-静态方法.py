"""
语法：
class Demo:
    @staticmethod
    def fn():
        pass

调用：
类名.fn()  一般使用这种方式
对象名.fn()
"""


class Demo:
    @staticmethod
    def info():
        print('info')


# 调用
Demo.info()
Demo().info()


"""
方法选择：
1. 如果你不知道用什么方法，你就直接用对象方法
2. 如果一个方法中，要使用对象属性，那么就定义为对象方法
3. 如果一个方法中，要使用类属性，那么就定义为类方法
4. 如果一个方法中，既没有使用类属性，也没有使用对象属性，那么就可以定位静态方法
"""