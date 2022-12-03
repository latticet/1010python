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


