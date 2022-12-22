# 传统文件读写操作
# 打开文件
# open(文件路径, mode='r', encoding='utf8')
# 操作文件
# 读
# read(size)  不写size,一次性读取全部。 写size:1.文本读字符个数。 2.二进制读。字节大小
# readline()  每次读取一行
# reanlines() 一次性读取所有行， 返回列表。每行是列表的一个元素
# 写
# write()
# writeline(['xx', 'xx'])
# 关闭文件
# f.close()

# 上下文管理器文件操作
"""
with open(文件路径, mode='r', encoding='utf8') as f:
    # 文件操作
"""

with open('resource/demo.txt', 'w', encoding='utf8') as f:
    f.write('hello world')

# 文件夹文件操作
import os
# 获取资源的绝对路径
print(os.path.abspath('04-函数.py'))
# 获取当前脚本的绝对路径
print(os.path.abspath(__file__))

# 动态获取
# 获取当前文件所在目录的路径
print(os.path.dirname(os.path.dirname(__file__)))
