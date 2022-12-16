"""
创建目录
删除目录（空目录或非空目录）
查找目录中是否存在某个文件
"""
import os
import shutil


class Directory:
    @staticmethod
    def mkdir(dirname):
        """创建目录"""
        os.mkdir(dirname)

    @staticmethod
    def rmdir(dirname):
        """删除目录"""
        shutil.rmtree(dirname)

    @staticmethod
    def is_file_in_dir(dirname, filename):
        """
        查找目录中是否存在某个文件
        :param dirname: 要查找目录的目录名
        :param filename: 是否在目录中存在的文件名
        :return:
        """
        # os.listdir(dirname) 查看目录下的所有资源，返回[]
        return filename in os.listdir(dirname)


# 创建目录
# Directory.mkdir('dir1')

# 查找目录中是否存在某个文件
# print(Directory.is_file_in_dir('dir1', 'demo1.txt'))
# print(Directory.is_file_in_dir('dir1', 'demo2.txt'))


# 删除目录
Directory.rmdir('dir1')

