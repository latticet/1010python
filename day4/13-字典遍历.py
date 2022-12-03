dict1 = {'name': 'hello', 'age': 18}
# 遍历key
# 第一种
for key in dict1.keys():
    print(key)
print('--' * 20)
# 第二种
for key in dict1:
    print(key)
print('==' * 20)

# 遍历value
for value in dict1.values():
    print(value)

# 遍历key和value
for key,value in dict1.items():
    print(key, value)
