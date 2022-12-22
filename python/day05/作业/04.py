"""
假设有一个列表 names = [[“张飞”,”刘备”,”关羽”],[“曹操”,”典韦”,”司马懿”]],
如何将names这个列表通过代码
转变得到如下列表 li=[“张飞”,”刘备”,”关羽”,“曹操”,”典韦”,”司马懿”]
"""

# 准备数据
li = []
names = [['张飞', '刘备', '关羽'], ['曹操', '典韦', '司马懿']]

# 第一种
# 遍历names列表
for name_list in names:
    for name in name_list:
        li.append(name)

print(li)

# 第二种
name1, name2 = names
name1.extend(name2)
print(name1)
