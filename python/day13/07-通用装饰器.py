# 装饰器定义
def decorator(fn):
    def inner(*args, **kwargs):
        # 前置扩展
        print('运算中...')
        result = fn(*args, **kwargs)
        # 后置扩展
        return result

    return inner


@decorator
def total(a, b, c, d):
    return a + b + c + d


print(total(1, 2, 3, 4))
