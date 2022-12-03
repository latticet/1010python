# dict
# 第一种（常用）
# 空字典
dict1 = {}
# 有数据据
# {key1:value1, key2:value2, ...}
dict2 = {'name': 'hello', 'age': 18}
print(dict1, dict2)
print(type(dict1), type(dict2))
print('==' * 20)

# 第二种
# 空字典
dict3 = dict()
# 有数据
dict4 = dict(name='hello', age=18)
print(dict3, dict4)
print(type(dict3), type(dict4))

"""
说明：
1. 字典的结构是key-value形式
2. 字典中的value可以存储任何数据类型且不唯一
3. 字典中的key是唯一的。一般都写字符串。
"""

dict5 = {'name': 'hello', 'name': 'good', (1, 2): '12'}
print(dict5)
