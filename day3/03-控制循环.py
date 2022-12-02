# 控制循环退出
# 这2个关键字只能在循环体中使用
# TODO continue
# 退出本次循环，下次循环继续
# 循环5次
"""
i = 1
while i < 6:
    if i == 3:
        i += 1
        continue

    print(i)
    i += 1
"""
# TODO break
# 退出整个循环（终止循环）
i = 1
while i < 6:
    if i == 3:
        break
    print(i)
    i += 1

