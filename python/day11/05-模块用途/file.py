import os


class File:
    @staticmethod
    def read(filename):
        """读取文件内容"""
        f = open(filename, 'r', encoding='utf8')
        content = f.read()
        f.close()
        return content

    @staticmethod
    def write(filename, content):
        """写入内容到文件中"""
        f = open(filename, 'w', encoding='utf8')
        f.write(content)
        f.close()
        print('写入成功...')

    @staticmethod
    def copy(filename):
        """复制文件"""
        # 通过源文件构建新文件名称
        source_filename, extension = os.path.splitext(filename)  # ('demo', '.txt')
        target_filename = source_filename + '-副本' + extension

        # 打开源文件，打开目标文件
        source_file = open(filename, 'rb')
        target_file = open(target_filename, 'wb')

        # 从源文件每次读取1KB写入目标文件
        while True:
            content = source_file.read(1024)
            if not content:
                break
            target_file.write(content)

        # 关闭文件
        source_file.close()
        target_file.close()

    @staticmethod
    def del_file(filename):
        """删除文件"""
        os.remove(filename)

    @staticmethod
    def rename(source_filename, target_filename):
        """文件改名"""
        os.rename(source_filename, target_filename)


if __name__ == '__main__':
    # 写入文件
    File.write('demo.txt', '123\n456')
    # 读取内容
    print(File.read('demo.txt'))
    # 复制内容
    File.copy('demo.txt')
    # 修改文件名
    File.rename('demo.txt', 'mydemo.txt')
    # 删除文件
    File.del_file('mydemo.txt')

"""
__name__:
第一种情况【脚本方式】：如果当前文件以脚本方式运行，__name__的值是 __main__
第二种方式【模块方式】：如果当前文件被导入方式运行，__name__的值是 模块名
"""
