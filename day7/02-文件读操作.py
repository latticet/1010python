# TODO f.read()
# 说明：一次性读取所有内容
# 语法：
'''
f.read(n=-1)
n=-1: 一次性读取所有内容
n=int
    1. 文本操作：按照字符个数进行读取.不区分字母和汉字
    2. 二进制操作：按照字节大小进行读取。  3Bytes = 1汉字   1024Bytes = 1KB  1MB = 1024KB  1G = 1024MB

'''
# 文本模式
'''
# 打开文件
f = open('resource/demo1.txt', 'r', encoding='utf8')
# 操作文件"""
# 文本方式读
# 没有参数的情况， 一次性读取所有内容
"""
content = f.read()
print(content)
"""
# 有参数的情况，按照字符个数去读
content = f.read(4)
print(content)

# 关闭文件
f.close()
'''

"""
# 二级制模式
# 打开文件
# 注意：如果是二进制模式就不需要加字符集
f = open('resource/demo1.txt', 'rb')
# 读取文件
content = f.read(6)
# 将Bytes类型转化为字符串类型
# 语法：bytes.decode()
# 字符串转bytes类型
# 语法：str.encode()
print(content)
print(content.decode())

str1 = content.decode()
print(str1.encode())
# 关闭文件
f.close()
"""

# TODO f.readline()
"""
# 每次读取一行内容
# 打开文件
f = open('resource/demo1.txt', 'r', encoding='utf8')
# 操作文件
while True:
    content = f.readline()
    if not content:
        break
    print(content, end='')
# 关闭文件
f.close()
"""
# TODO f.readlines()
# 说明：一次性读取所有行，返回列表。将每一行的内容放到列表中
f = open('resource/demo1.txt', 'r', encoding='utf8')
lines = f.readlines()
print(lines)
f.close()
