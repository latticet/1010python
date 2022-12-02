"""
使用if，编写程序，实现以下功能：
l 从键盘获取用户名、密码
l 如果用户名和密码都正确（预先设定一个用户名和密码），那么就显示“欢迎进入xxx的世界”，否则提示密码或者用户名错误
"""

# 预设账号密码
sys_username = 'admin'
sys_password = '123456'

# 用户输入
username = input('账号：')
password = input('密码：')

# 执行流程
if username == sys_username and password == sys_password:
    print(f'欢迎进入{username}的世界')
else:
    print('用户名或者密码错误')
