# 论坛
# 认证登录的装饰器
def check_login(fn):
    def inner():
        print('登录认证')
        return fn()

    return inner


# 发布文章
@check_login
def post():
    # 登录
    print('发布文章')


# 评论文章
@check_login
def comment():
    # 登录
    print('评论文章')


# ...

post()

comment()
