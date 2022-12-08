"""
文件操作模式：
r(read): 读操作
w(write)：覆盖写，文件不存在创建
a(append): 追加写，文件不存在创建

b(binary): 二进制模式，不能单独使用。必须配合读写模式
+：扩展模式，不能单独使用。
"""
# TODO a模式
"""
# 打开文件
f = open('resource/demo4.txt', 'a', encoding='utf8')
# 操作文件
f.write('555')
# 关闭文件
f.close()
"""

# TODO b模式
"""
# 打开文件
f = open('resource/demo4.txt', 'wb')
# 操作文件
bytes_str = '555'.encode()
f.write(bytes_str)
# 关闭文件
f.close()
"""

# TODO +模式
"""
# 打开文件
f = open('resource/demo4.txt', 'r+', encoding='utf8')
# 操作文件
# 读取内容
content = f.read()
print(content)
# 写入内容
f.write('\n777')
# 关闭文件
f.close()
"""
"""
# 打开文件
f = open('resource/demo4.txt', 'w+', encoding='utf8')
# 操作文件
# 读取内容
content = f.read()
print(content)
# 写入内容
f.write('\n777')
# 关闭文件
f.close()
"""

"""
# 打开文件
f = open('resource/demo4.txt', 'a+', encoding='utf8')
# 操作文件
# 读取内容
content = f.read()
print(content)
# 写入内容
f.write('\n777')
# 关闭文件
f.close()
"""

f = open('resource/demo5.txt', 'w+', encoding='utf8')
# 操作文件
# 写入内容
f.write('你好')

# 移动光标到最左边
# 语法：f.seek(size)  size:距离左边的字节大小
f.seek(3)

# 读取内容
content = f.read()
print(content)

# 关闭文件
f.close()
