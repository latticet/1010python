"""
封装函数，设计根据QQ和密码登录的过程(QQ和密码预设为指定的值).
执行结果为登录是否成功(boolean类型的值)
"""


def login():
    # 系统账号密码
    sys_username = 'admin'
    sys_password = '123456'

    # 用户输入信息
    username = input('username:')
    password = input('password:')

    return sys_username == username and sys_password == password


print(login())
