# 导入pandas
import pandas as pd

# 读取excel文件
# 语法： pd.read_excel(文件路径, sheet_name) 默认读取第一个sheet
data = pd.read_excel('data/sales.xlsx', '2018')
print(data)

# 获取数据形状
print(data.shape)

# 获取数据索引
print(data.index)

# 获取数据字典
print(data.columns)

