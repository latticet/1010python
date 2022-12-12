"""
网吧年龄验证
需求：
1. 定义两个变量，分别记录年龄和是否携带身份证
2. 如果满18岁，并且带有身份证，运行进入网吧上网。
"""
# 接收用户输入
age = int(input('年龄：'))
is_card = int(input('是否携带身份证：[1：yes|2：no]'))

# 根据条件执行逻辑
if age >= 18:
    if is_card == '1':
        print('可以上网')
    else:
        print('不可以上网')
else:
    print('不可进入')
