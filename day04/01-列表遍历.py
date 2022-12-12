# 遍历
# 循环获取列表中的元素

list1 = ['python', 'mysql', 'linux', 'shell']
"""
print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])
"""
# TODO while循环遍历
i = 0
while i < len(list1):
    print(list1[i])
    i += 1
print('==' * 20)

# TODO for循环遍历[常用]
"""
可迭代对象：str， list
语法：
for 临时变量 in 可迭代对象:
    临时变量
说明：
临时变量：可迭代对象中的元素
"""

# list
list1 = ['python', 'mysql', 'linux', 'shell']
for item in list1:
    print(item)
print('==' * 20)

# str
str1 = 'hello'
for char in str1:
    print(char)


