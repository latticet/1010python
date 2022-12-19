def demo2():
    print('demo2')


# 开始时间
# demo2()
# 结束时间
# 结束时间 - 开始时间


# TODO 装饰器定义
# 说明：装饰器是一个特殊的闭包
# fn: 被装饰的那个函数
def wrapper(fn):  # fn =  demo1
    def inner():
        print('开始时间')
        fn()
        print('结束时间')

    return inner


def demo1():
    print('demo1')


# TODO 使用装饰器（装饰）
# 对demo1进行装饰
demo1 = wrapper(demo1)  # demo1 = inner
demo1()
