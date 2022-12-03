# 元组获取
t1 = ('python', 'mysql', 'linux', 'git')

# TODO 索引
print(t1[1])
print(t1[-3])

# TODO 切片
print(t1[:2])
print(t1[-4:2])

# 元组修改：不可变数据类型
# t1[1] = 'java'
# 元组是不可以修改的
# TODO 遍历
for item in t1:
    print(item)

