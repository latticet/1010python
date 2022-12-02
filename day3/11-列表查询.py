# TODO 通过索引获取值
# 语法： list[index]
list1 = ['mysql', 'linux', 'git', 'linux']
print(list1[-2])
print('==' * 20)

# TODO list.index(数据) 通过数据查询元素的下标，如果数据不存在，抛出错误
print(list1.index('linux'))
# list1.index('shell')
print('==' * 20)

# TODO len(list|str) 获取列表长度
print(len(list1))
print(len('hello'))
print('==' * 20)

# TODO list.count(数据) 获取数据在列表中出现的次数
print(list1.count('linux'))
print(list1.count('mysql'))
print(list1.count('shell'))
