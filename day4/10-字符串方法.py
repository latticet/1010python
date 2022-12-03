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
str1 = 'hello'
# str.upper()  转大写
str2 = str1.upper()
print(str2)
# str.lower()  转小写
print(str2.lower())
# str.title() 单词首字母大写
str3 = 'hello,good,fine'
print(str3.title())


