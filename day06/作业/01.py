"""
for循环实现99乘法表
"""
"""
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
"""
for j in range(5):
    for i in range(5):
        print('*', end=' ')
    print()
print('==' * 20)

"""
* 
* * 
* * * 
* * * * 
* * * * *
"""
"""
for i in range(1, 2):
    print('*', end=' ')
print()

for i in range(1, 3):
    print('*', end=' ')
print()

for i in range(1, 4):
    print('*', end=' ')
print()

for i in range(1, 5):
    print('*', end=' ')
print()
"""

for j in range(1, 6):
    for i in range(1, j + 1):
        print('*', end=' ')
    print()
print('==' * 20)

"""
99乘法表
"""
for j in range(1, 10):
    for i in range(1, j + 1):
        print(f'{i} * {j} = {i * j}', end='\t')
    print()
