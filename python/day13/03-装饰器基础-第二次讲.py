# 装饰器是一个特殊的闭包
# wrapper传入的参数必须是一个函数，这个函数就是我们要装饰的函数

# 定义装饰器
def wrapper(fn):
    def inner():
        print('前置扩展功能')
        fn()
        print('后置扩展功能')

    return inner


def demo():
    print('demo')


# 使用装饰器 (对函数进行装饰)
# wrapper这个装饰器对demo这个函数进行装饰
demo = wrapper(demo)

demo()
