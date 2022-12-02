# TODO list.insert(索引, 数据)  指定索引添加数据
list1 = ['python', 'mysql']
# 添加linux到索引1位置
list1.insert(1, 'linux')
print(list1)

list1.insert(-2, 'git')  # ['python', 'linux', 'git', 'mysql']
print(list1)
print('==' * 20)

# TODO list.append(数据) 将整个数据追加到列表末尾
list2 = ['python', 'mysql']
list2.append('linux')
list2.append('shell')
list2.append(['hello', 'good'])
print(list2)
print('==' * 20)


# TODO list.extend(数据) 将数据中的元素依次追加到列表末尾
# 说明：
# 数据：字符串类型 或者 列表
list3 = ['python', 'mysql']
list3.extend(['hello', 'good'])
list3.extend('hello')
print(list3)
