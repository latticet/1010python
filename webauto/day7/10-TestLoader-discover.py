from unittest import defaultTestLoader, TextTestRunner


# 创建loader
# 导入case目录下，以_testcase.py结尾的文件
suite = defaultTestLoader.discover('case', pattern='*_testcase.py')

# 创建runner
runner = TextTestRunner()
runner.run(suite)