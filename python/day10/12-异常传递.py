# TODO　函数嵌套
def fn1():
    try:
        result = 1 / 0
    except ZeroDivisionError:
        print('Zero')


def fn2():
    fn1()


def fn3():
    fn2()


fn3()

# TODO 异常语句嵌套
try:
    try:
        try:
            result = 1 / 0
        except ValueError as e:
            print(e)
    except NameError as e:
        print(e)
except ZeroDivisionError as e:
    print(e)
