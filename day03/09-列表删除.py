# TODO del list[index] 通过索引删除执行元素
list1 = ['mysql', 'linux']
del list1[0]
print(list1)
print('==' * 20)

# TODO list.remove(元素) 删除第一个指定的元素
list2 = ['mysql', 'linux', 'git', 'linux']
list2.remove('linux')
print(list2)
print('==' * 20)

# TODO list.pop([索引]) 通过索引弹出对应元素，如果没有指定元素，那么弹出最后一个元素
# 弹出：删除并返回
list3 = ['mysql', 'linux', 'git', 'linux']
# 不指定下标
print(list3.pop())
print(list3)
print('--' * 20)
# 指定下标
print(list3.pop(-2))
print(list3)
print('==' * 20)

# TODO list.clear()  清空列表
list4 = ['mysql', 'linux', 'git', 'linux']
list4.clear()
print(list4)

