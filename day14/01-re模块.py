import re

# TODO search(pattern,string[,flags])
# 说明：在字符串中查找正则匹配的字符串，返回第一个匹配到的对象或者None

# 返回第一个匹配到的对象
match_obj = re.search('he', 'hello hello')
print(match_obj)

# Match.group()
# 获取匹配到的字符串
print(match_obj.group())

# 返回None:匹配不到
result = re.search('ab', 'hello')
print(result)
print('==' * 20)

# TODO findall(pattern, string[,flags])
# 说明：列出字符串中模式的所有匹配项,返回所有匹配到的字符串列表
match_list = re.findall('he', 'hello hello')
print(match_list)

match_list = re.findall('ab', 'hello hello')
print(match_list)
