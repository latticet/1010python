# 元组：tuple
# TODO 第一种[常用]
# 空元组
t1 = ()
# 有数据元组
t2 = ('hello', 'good', 10, True, None, [1, 2])
print(t1)
print(t2)
print(type(t1), type(t2))

# 注意：
# 如果元组中只有一个元素，后面必须加逗号。
t3 = ('python',)
print(t3, type(t3))
print('==' * 20)

# TODO 第二种
# 空元组
t4 = tuple()
# 有数据的元组
t5 = tuple('hello')
t6 = tuple(['python', 'good'])
print(type(t4), type(t5), type(t6))
print(t4)
print(t5)
print(t6)

"""
说明：y
1. 元组中的数据叫做元素
2. 元组中可以存放任何数据类型
3. 元组中的元素是可以重复的
4. 元组是有序的：索引
"""
