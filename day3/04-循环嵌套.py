"""
语法：
while 条件:
    while 条件:
        代码块
"""

# 需求1 ：
"""
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
"""

j = 0
while j < 5:
    i = 0
    while i < 5:
        print('*', end=' ')
        i += 1
    print()  # end='\n'
    j += 1

print('==' * 20)

# 需求2：
"""
* 
* * 
* * * 
* * * * 
* * * * *
"""
"""
# 1 *
i = 0
while i < 1:
    print('*', end=' ')
    i += 1
print()

# 2 *
i = 0
while i < 2:
    print('*', end=' ')
    i += 1
print()

# 3 *
i = 0
while i < 3:
    print('*', end=' ')
    i += 1
print()
"""
# 第一种
j = 0
while j < 5:

    i = 0
    while i <= j:
        print('*', end=' ')
        i += 1
    print()

    j += 1
print('==' * 20)

# 第二种
j = 1
while j <= 5:

    i = 1
    while i <= j:
        print('*', end=' ')
        i += 1
    print()

    j += 1