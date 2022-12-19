import random

# random.random()	实数相关	用于生成一个0到1的随机浮点数: [0, 1)
"""
print(random.random())
"""

# random.uniform(a,b)		生成[a,b]或[b,a]之间的均匀分布随机浮点数。
"""
print(random.uniform(1, 5))
"""

# random.randint(a,b)	整数相关	生成[a,b]的随机整数，要求a < b。
"""
for i in range(10):
    print(random.randint(1, 10))
"""

# random.randrange(a,b,step)		生成[a,b)的随机整数，第三个参数可以指定步长。
"""
for i in range(10):
    print(random.randrange(2, 10, 2))
"""

# random.choice(seq)	序列相关	从序列中随机选择一个元素，若序列为空，则抛出异常。
# 序列：str tuple list
"""
# tuple
print(random.choice((1, 2, 3)))
# list
print(random.choice(['linux', 'python', 'mysql']))
# str
print(random.choice('hello'))
"""

# random.shuffle(seq)		打乱原序列，原序列必须可写。
# 可写序列：list
"""
list1 = ['linux', 'mysql', 'python']
random.shuffle(list1)
print(list1)
"""

# random.sample(seq,k)		从序列中随机选择k个元素返回，原序列不变。
list1 = ['linux', 'mysql', 'python', 'git', 'shell']
print(random.sample(list1, 2))

# random.seed(n=none)	初始化	初始化随机熵池。
