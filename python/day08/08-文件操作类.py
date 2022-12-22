"""
类名：File
属性：
    f:打开的文件资源句柄
方法:
    read
    write
"""


class File:
    def __init__(self, filename, mode, encoding=None):
        file_path = f'resource/{filename}'
        self.f = open(file_path, mode, encoding=encoding)

    def read(self):
        return self.f.read()

    def write(self, content):
        self.f.write(content)

    def seek(self, size=0):
        self.f.seek(size)

    def __del__(self):
        self.f.close()


file = File('demo1.txt', 'w+', 'utf8')
file.write('123\n567\n')
file.seek()
print(file.read())
