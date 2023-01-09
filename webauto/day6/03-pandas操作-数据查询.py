import pandas as pd

# TODO data.loc 根据行、列的标签值查询
# 语法：data.loc[行标签， 列标签]

# 读取数据
data = pd.read_csv('data/lj_data.csv')

# 第二行数据
# print(data.loc[1])

# 广安门租房
# print(data.loc[2, '区域'])

# 1-5行
# print(data.loc[[0, 1, 2, 3, 4]])

# 1-5行， 区域,地址,标题,户型
# print(data.loc[[0, 1, 2, 3, 4], ['区域', '地址', '标题', '户型']])


# TODO data.iloc 根据行和列的索引来查询数据
# 语法：data.iloc[行索引, 列索引]
# 第二行数据
# print(data.iloc[1].values)

# 广安门租房
# print(data.iloc[2,0])

# 1-5行
# print(data.iloc[[0, 1, 2, 3, 4]].values)

# 1-5行， 区域,地址,标题,户型
print(data.iloc[[0, 1, 2, 3, 4], [0, 1, 2, 3]].values)
