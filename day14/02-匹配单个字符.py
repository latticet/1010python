import re

"""
原字符：字符本身的含义
元字符: 具有特殊含义字符
"""

# TODO 原字符
print(re.search('he', 'hello').group())
print('--' * 20)

# TODO . 匹配任意1个字符（除了\n）
print(re.search('h.', 'hello').group())
print(re.search('h.', 'h+llo').group())
print(re.search('h.', 'h%llo').group())
print(re.search('h.', 'h1llo').group())
print(re.search('h.', 'h\nllo'))  # 不能匹配
print('--' * 20)

# TODO [ ]	匹配[ ]中列举的一个字符[0-9][a-z][A-Z][\u4e00-\u9fa5]
print(re.search('h[abc]', 'ha123').group())
print(re.search('h[abc]', 'hb123').group())
print(re.search('h[-+=]', 'h+123').group())
print(re.search('h[123]', 'h3123').group())

# [0-9]匹配0到9之间的任意一个字符
print(re.search('h[0-9]', 'h1bb').group())
# [a-z]匹配a-z之间的任意一个字符
print(re.search('h[a-z]', 'hfa').group())
# [A-Z]匹配A-Z之间的任意一个字符
print(re.search('h[A-Z]', 'hT').group())
print(re.search('h[A-Z]', 'ht'))  # 匹配不到
# [\u4e00-\u9fa5] 匹配任意一个汉字
print(re.search('[\u4e00-\u9fa5]', '你好').group())
print(re.search('[\u4e00-\u9fa5]', 'hello'))  # 匹配不到
# 可以同时多组使用
print(re.search('[a-zA-Z0-9]', '1').group())
print(re.search('[a-zA-Z0-9]', 'F').group())
print(re.search('[a-zA-Z0-9]', 'c').group())
print('--' * 20)

# TODO \d 匹配数字，即0-9   [0-9]
print(re.search('h\d', 'h0').group())
print(re.search('h\d', 'h8').group())
print(re.search('h\d', 'h5').group())
print('--' * 20)

# TODO \D 匹配非数字，即不是数字
print(re.search('h\D', 'h+').group())
print(re.search('h\D', 'hF').group())
print(re.search('h\D', 'h&').group())
print(re.search('h\D', 'h0'))
print('--' * 20)

# TODO \s 匹配空白，即 空格，tab键, \n
print(re.search('h\s', 'h ').group())
print(re.search('h\s', 'h   ').group())
print(re.search('h\s', 'h\n').group())
print(re.search('h\s', 'ha'))
print('--' * 20)

# TODO \S 匹配非空白
print(re.search('h\S', 'ha').group())
print(re.search('h\S', 'h1').group())
print(re.search('h\S', 'h+').group())
print(re.search('h\S', 'h|').group())
print(re.search('h\S', 'h '))
print('--' * 20)

# TODO \w 匹配非特殊字符，即a-z、A-Z、0-9、_、汉字
# 相当于：[0-9a-zA-Z_\u4e00-\u9fa5]
print(re.search('h\w', 'h1').group())
print(re.search('h\w', 'ha').group())
print(re.search('h\w', 'h_').group())
print(re.search('h\w', 'h你').group())
print(re.search('h\w', 'h-'))
print(re.search('h\w', 'h$'))


# TODO \W 匹配特殊字符
