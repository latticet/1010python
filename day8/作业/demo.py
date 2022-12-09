import os

# 输入源文件
filename = input('要复制的文件:')
# 切换到resource
os.chdir('resource')
# 构造目标文件名称
source_filename, extension = os.path.splitext(filename)
target_filename = source_filename + '-副本' + extension

# 打开源文件， 打开目标文件
source_file = open(filename, 'rb')
target_file = open(target_filename, 'wb')

# 通过固定大小，循环读取源文件内容，写入目标文件
while True:
    content = source_file.read(1024)
    if not content:
        break
    target_file.write(content)

# 关闭文件
source_file.close()
target_file.close()
