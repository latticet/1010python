def wrapper(fn):
    def inner():
        print('前置扩展')
        fn()
        print('后置扩展')

    return inner


# 在要装饰的函数上面用@写装饰器就进行了装饰
@wrapper
def demo1():  # demo = wrapper(demo)
    print('demo1')


@wrapper
def demo2():
    print('demo2')


# wrapper装饰器对demo这个函数进行了装饰
# demo = wrapper(demo)

demo1()
demo2()
