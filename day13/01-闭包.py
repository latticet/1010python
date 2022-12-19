# 闭包
def fn1():
    num1 = 100

    def fn2():
        print(num1)

    return fn2

# 作用域
# 函数体中的作用域：局部作用域
fn2 = fn1()
fn2()



