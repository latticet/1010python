"""
语法：
print(['content1', 'content2', 'content_n', sep=' ', end='\n'])
sep: 多个输出内容之间的分隔符，默认是空格
end: 输出的结尾符，默认是\n，\n就是换行
说明：
1. print是一个函数
2. 在函数中传入的内容，叫做参数
3. 在python中单引号和双引号没有区别。
作用：
输出内容
使用：
编码风格：
python官方编码规范：PEP8
"""
# 输出多个内容
print('python', 'mysql', 'linux', 'shell')

# 输出多个内容，修改sep参数
print('python', 'mysql', 'linux', 'shell', sep='-')

# 输出内容，修改结尾符
print('apple', end='|')
print('huawei')
