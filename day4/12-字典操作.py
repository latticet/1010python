# TODO 字典添加
# 语法： dict[key] = value
dict1 = {'name': 'hello'}
dict1['age'] = 18
print(dict1)
print('==' * 20)

# TODO 字典修改
# 语法： dict[key] = new_value
dict1['age'] = 20
print(dict1)
print('--' * 20)

# dict.setdefault(key, value)
# 1. 如果key不存在，就设置value，并返回
print(dict1.setdefault('addr', '成都'))
print(dict1)
# 2. 如果key存在，就不设置，返回原value
print(dict1.setdefault('addr', '重庆'))
print(dict1)
print('--' * 20)

# dict1.update(dict2) 将dict2的数据合并到dict1。如果key相同就覆盖。
dict1 = {'name': 'hello', 'age': 18}
dict2 = {'name': 'good', 'addr': '成都'}
dict1.update(dict2)
print(dict1)
print('==' * 20)

# TODO 字典删除
dict1 = {'name': 'hello', 'age': 18}
# del dict[key] 通过key删除对应数据
del dict1['name']
print(dict1)
print('--' * 20)

# dict.pop(key) 弹出key对应的value，并删除
dict1 = {'name': 'hello', 'age': 18}
print(dict1.pop('name'))
print(dict1)
print('--' * 20)

# dict.clear() 清空字典
dict1 = {'name': 'hello', 'age': 18}
dict1.clear()
print(dict1)
print('==' * 20)

# 字典查询
# dict[key] 通过key过去对应的值，如果key不存在会报错
dict1 = {'name': 'hello', 'age': 18}
print(dict1['name'])
print(dict1['age'])
# print(dict1['addr'])
print('--' * 20)

# dict.get(key[, None]) 通过key获取对应的值.如果key不存在返回第二个参数的值，默认为None
# key存在
print(dict1.get('name'))
print(dict1.get('age'))
# key不存在
print(dict1.get('addr'))  # None
print(dict1.get('addr', '成都'))  # 成都
print('--' * 20)

# len(容器)  str, list, tuple, dict 获取容器长度
print(len(dict1))
print('--' * 20)


dict1 = {'name': 'hello', 'age': 18}
# 获取所有key  dict.keys()
print(dict1.keys())
# 获取所有value dict.values()
print(dict1.values())
# 获取所有key和value dict.items()
print(dict1.items())
print('--' * 20)

# in 语句
# 元素是否在容器中 是就是True 否就是False、
# 语法： 元素 in 容器
dict1 = {'name': 'hello', 'age': 18}
# 查看key在不在字典中
# 第一种
print('name' in dict1.keys())
# 第二种
print('name' in dict1)
# 查看value在不在字典中
print('hello' in dict1.values())

# list
print('hello' in ['hello', 'good'])
print('hello1' in ['hello', 'good'])








