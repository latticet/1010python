import re

# 需求：
# 验证用户输入的是否是手机号
# 接收用户输入


phone = input('手机号：')
if re.search('^1[2-9]\d{9}$', phone):
    print('手机格式正确')
else:
    print('手机格式错误')

# 限定符
# TODO 限定开始
# ^	匹配字符串开头
# 匹配以he开头的字符
print(re.search('^he', 'hello').group())
print(re.search('^he', '1hello'))
print('--' * 20)

# TODO 限定结束
# $	匹配字符串结尾
# 匹配以he结尾的字符
print(re.search('he$', 'abc_he').group())
print(re.search('he$', '11c_he').group())
print(re.search('he$', '11c_he1'))

# ^ 和 $ 一起使用
# 匹配hello
print(re.search('^hello$', 'hello').group())
print(re.search('^hello$', '1hello'))
print(re.search('^hello$', 'hello2'))
