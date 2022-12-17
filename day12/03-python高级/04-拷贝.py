import copy

# TODO 浅拷贝
# 说明：只拷贝对象的最外层
# 使用：copy.copy()
# 可变数据类型
list1 = ['python', 'mysql', [1, 2]]
list2 = copy.copy(list1)
print(f'list1:{id(list1)}|list1[2]:{id(list1[2])}')
print(f'list2:{id(list2)}|list2[2]:{id(list2[2])}')
print('--' * 20)
# 不可变数据类型
str1 = 'hello'
str2 = copy.copy(str1)
print(f'str1:{id(str1)}')
print(f'str2:{id(str2)}')
print('==' * 20)

# TODO 深拷贝
# 说明：拷贝对象的所有层级
# 使用：copy.deepcopy()
list1 = ['python', 'mysql', [1, 2]]
list2 = copy.deepcopy(list1)
print(f'list1:{id(list1)}|list1[2]:{id(list1[2])}')
print(f'list2:{id(list2)}|list2[2]:{id(list2[2])}')


list1 = [1, 2]
list2 = copy.deepcopy(list1)