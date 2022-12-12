# TODO 去除两边空格
"""
str1 = input('字符串：')
print(f'原生字符串:{str1}')
# str.lstrip()  去除左边空格
print(str1.lstrip())
# str.rstrip()  去除右边空格
print(str1.rstrip())
# str.strip()   去除两边空格
print(str1.strip())
"""

# TODO 字符串分割， 字符串转列表
# str.split('分割符号'[, '分割次数'])  返回列表.从左至右进行分割
"""
str1 = 'hello,good,fine'
print(str1.split(','))
print(str1.split(',', 1))
print('--' * 20)

# str.rsplit('分割符号'[, '分割次数']) 从右至左进行分割
print(str1.rsplit(','))
print(str1.rsplit(',', 1))
"""

# TODO 大小写转换
"""
str1 = 'hello'
# str.upper()  转大写
str2 = str1.upper()
print(str2)
# str.lower()  转小写
print(str2.lower())
# str.title() 单词首字母大写
str3 = 'hello,good,fine'
print(str3.title())
"""

# TODO 判断开头或结尾
"""
str1 = 'hello'
# str.startswith('字符串')   是否以某字符串开始
print(str1.startswith('he'))
print(str1.startswith('ab'))
print('--' * 20)

# str.endswith('字符串')   是否以某字符串结尾
print(str1.endswith('llo'))
print(str1.endswith('llb'))
print('==' * 20)
"""

# TODO 字符串格式化
# str.format()   字符串格式化函数
"""
name = 'hello'
age = 18
# 第一种 默认顺序
str1 = '姓名：{};年龄：{}'.format(name, age)
print(str1)
# 第二种 指定顺序
str1 = '姓名：{0};年龄：{1}'.format(name, age)
print(str1)
# 第三种 指定名字
str1 = '姓名：{name};年龄：{age}'.format(name=name, age=age)
str2 = '姓名：{name};年龄：{age}'.format(name='good', age=20)
print(str1)
print(str2)
"""

# TODO 字符串拼接
# str.join(list)  列表转字符串
"""
list1 = ['python', 'mysql', 'linux']
str1 = '-'.join(list1)
str2 = ','.join(list1)
str3 = ' '.join(list1)
str4 = ''.join(list1)
print(str1)
print(str2)
print(str3)
print(str4)
"""

# TODO 字符串替换
# str.replace(原内容，新内容)  全部替换
"""
str1 = 'hello python, 你好 python'
str2 = str1.replace('python', 'mysql')
print(str2)
"""

# TODO 判断字符串构成
# 判断字符串由数字组成 str.isdigit()
print('123'.isdigit())
print('a23'.isdigit())
print('--' * 20)
# 判断字符串由字母组成 str.isalpha()
print('abc'.isalpha())
print('a23'.isalpha())
print('123'.isalpha())
print('--' * 20)
# 判断字符串由字母或数字组成
print('abc'.isalnum())
print('a23'.isalnum())
print('123'.isalnum())


