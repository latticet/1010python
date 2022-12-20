import re

# TODO 贪婪模式
# 说明：默认正则在使用量词匹配的时候，会尽可能多的匹配。这种情况叫做贪婪模式
str1 = '<div></div><span></span><font></font>'
print(re.search('<.{3,}>', str1).group())
print(re.findall('<.{3,}>', str1))

# TODO 非贪婪模式
# 说明：在量词后面加？
str1 = '<div></div><span></span><font></font>'
print(re.search('<.{3,}?>', str1).group())
print(re.findall('<.{3,}?>', str1))

