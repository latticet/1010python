
list1 = [10, 11, 20, 8, 3]

# TODO list.sort([reverse=False]) reverse=False：升序， reverse=True：降序
# reverse=False默认
list1.sort()
print(list1)

# reverse=True
list1.sort(reverse=True)
print(list1)

list2 = ['apple', 'cool', 'bread',  'airdrop']
# 升序
# 对于字母来说，按照ASCII码排序
# 查看ASCII码
print(ord('a'))
list2.sort()
print(list2)


# TODO list.reverse()    列表反转
list2.reverse()
print(list2)

