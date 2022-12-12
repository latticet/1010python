# set
# TODO 定义
# 第一种
# 空集合
set1 = set()
# 有数据
set2 = set('abc')
print(set1)
print(set2)
print(type(set1))
print(type(set2))

# 第二种(常用)
set3 = {'python', 'java', 'golang', 'python'}
set4 = {}  # 空字典
print(set3)
print(type(set3), type(set4))
print('==' * 20)

# 集合是可变的
set3.add('c++')
print(set3)

# 集合中只能存不可变数据类型
# set4 = {'a', 12, {'a':1}}
# print(set4)

# TODO 特点
"""
1. 无序
2. 唯一
3. 可变数据类型：list，dict， set
4. 集合中只能存不可变数据类型
"""

# TODO 转化
# str -> set
print(set('abc'))
# tuple -> set
print(set(('aa', 'bbb', 'cccc')))
# list -> set
print(set(['hello', 'good', 'fine']))


