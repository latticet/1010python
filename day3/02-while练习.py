# 1. 输出1-100
# 计数器：
# 1. 控制循环次数
# 2. 参与运算
"""
i = 1
while i < 101:
    print(i)
    i += 1
"""
# 2. 输出1-100之间的所有偶数
"""
i = 1
while i <= 100:
    if i % 2 == 0:
        print(i)
    i += 1
"""
# 3. 输出1-100之间所有奇数的和
# 初始化一个用来统计结果的变量
total = 0
i = 1
while i < 101:
    if i % 2 != 0:
        total += i
    i += 1

print(total)