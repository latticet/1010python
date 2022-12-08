import os
import shutil

# TODO os.rename("文件路径","新文件名")
# 文件重命名
# 如果前面是文件路径，后面新文件也要指定相同路径
"""
os.rename('hello.txt', '你好.txt')
os.rename('resource/demo6.txt', 'resource/demo66.txt')
"""

# TODO  os.remove (文件路径)
# 删除文件
"""
os.remove('resource/demo66.txt')
os.remove('你好.txt')
"""

# TODO os.mkdir ("文件夹路径")
# 创建文件夹
"""
os.mkdir('resource/dir1')
"""
# TODO os.getcwd()
# 获取当前脚本所在的路径
"""
print(os.getcwd())
"""

# TODO  os.chdir()
# 切换目录
"""
print(os.getcwd())
os.chdir('../..')
print(os.getcwd())
"""

# TODO os.listdir("目录路径")
# 获取指定录下的资源名称，返回列表
"""
print(os.listdir('resource'))
"""

# TODO os.rmdir("目录路径")
"""
# 删除目录，只能删除空目录
os.rmdir('resource/dir1')
# 删除非空目录
shutil.rmtree('resource/dir1')
"""

# TODO  os.path.isdir("目录路径")
"""
# 判断资源是目录
print(os.path.isdir('resource/dir1'))  # True
print(os.path.isdir('resource/demo1.txt'))  # False

# TODO os.path.isfile("文件路径")
# 判断资源是文件
print(os.path.isfile('resource/demo1.txt'))
print(os.path.isfile('resource/dir1'))
"""

# TODO  os.path.splitext ("文件名")
# 获取文件扩展名，返回元组 （文件名, 后缀）
filename_path, extension = os.path.splitext('resource/demo1.txt')
print(filename_path)
print(extension)
