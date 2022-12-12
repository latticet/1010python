# 输入要复制的文件名
filename = input('文件名：')

# 打开要复制的文件
file_path = f'resource/{filename}'
source_f = open(file_path, 'r', encoding='utf8')

# demo1.txt  -> demo1 .txt  demo1-副本.txt
# hello.demo1.txt
# 根据源文件名，构造目标文件名
index = filename.rindex('.')
source_filename = filename[:index]
extension = filename[index:]
# 构建目标文件
target_filename = source_filename + '-副本' + extension

# 打开目标文件
target_f = open(f'resource/{target_filename}', 'w', encoding='utf8')

# 读取源文件的内容，写入目标文件
content = source_f.read()
target_f.write(content)

# 关闭资源
target_f.close()
source_f.close()
