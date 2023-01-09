"""
数据操作类：读取测试数据
类名：DataOperation
方法：
    init： 根据文件类型读取数据
    read_list: 提取为列表数据
    read_dict: 提取为字典数据
"""
import os
import pandas as pd


class DataOperation:
    def __init__(self, filename, sheet_name=0):
        # 判断文件后缀
        _, extension = os.path.splitext(filename)

        # 构建文件路径
        file_path = os.path.join(os.path.abspath('data'), filename)

        # 读取文件
        if extension == '.csv':
            # 如果传入.csv  data.read_csv()
            self.data = pd.read_csv(file_path)
        else:
            # 如果传入.xlsx  data.read_excel()
            self.data = pd.read_excel(file_path, sheet_name)

    def read_list(self):
        """提取为列表数据"""
        return self.data.values.tolist()

    def read_dict(self):
        """提取为字典数据"""
        # print(self.data.iloc[0].to_dict())
        # print(self.data.iloc[1].to_dict())
        # print(self.data.iloc[2].to_dict())

        # 语法：[形成列表元素的表达式 控制列表元素个数的表达式]
        return [self.data.iloc[i].to_dict() for i in self.data.index.values.tolist()]


if __name__ == '__main__':
    data = DataOperation('user_info.csv')
    # data.read_list()
    print(data.read_dict())
