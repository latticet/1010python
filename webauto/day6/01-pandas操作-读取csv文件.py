# 导入pandas
import pandas as pd

# 文本格式的数据
# csv: ,分隔符
# tsv: Tab分隔符
# txt: 没有固定格式

# 读取文本数据, 返回读取到的内容
# 语法： pd.read_csv(文件路径， [sep=','])
data = pd.read_csv('data/lj_data.csv')
# 默认查看前5行
# print(data.head())

# 查看数据形状  data.shape 返回(行, 列)
# print(data.shape)

# 查看字段名（表头名称）
# print(data.columns)

# 查看数据索引
print(data.index)


