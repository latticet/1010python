"""
读取一个py文件，显示除了以井号(#)开头的行以外的所有行
"""
# 打开文件
f = open('demo.py', 'r', encoding='utf8')
# 操作文件
lines = f.readlines()
for line in lines:
    if not line.startswith('#'):
        print(line, end=' ')
# 关闭文件
f.close()
