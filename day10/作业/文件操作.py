"""
定义一个文件操作类File，方法有：读取所有内容，读取数据按行返回，写入内容，追加数据。
有以下类方法：
File.read(文件名)
File.write(文件名,’内容’)
File.readlines(文件名)
File.append(文件名,’内容’)
"""


class File:
    @classmethod
    def read(cls, filename):
        """读取所有内容"""
        f = open(filename, 'r', encoding='utf8')
        content = f.read()
        f.close()
        return content

    @classmethod
    def write(cls, filename, content):
        """写入内容"""
        f = open(filename, 'w', encoding='utf8')
        f.write(content)
        f.close()

    @classmethod
    def readlines(cls, filename):
        """读取数据按行返回"""
        f = open(filename, 'r', encoding='utf8')
        lines = f.readlines()
        f.close()
        return lines

    @classmethod
    def append(cls, filename, content):
        """追加数据"""
        f = open(filename, 'a', encoding='utf8')
        f.write(content)
        f.close()


# 调用
File.write('demo.txt', '123\n456')
print(File.read('demo.txt'))
File.append('demo.txt', '\n789')
print(File.readlines('demo.txt'))
