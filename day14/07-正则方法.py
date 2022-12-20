import re

# TODO re.I 使匹配对大小写不敏感，也就是不区分大小写的模式l
# I: Ignore

print(re.search('Hello', 'hello', re.I))
print(re.search('Hello', 'Hello'))
print('==' * 20)

# TODO re.S 使.这个通配符能够匹配包括换行在内的所有字符，针对多行匹配
# S: Space
print(re.search('hello.world', 'hello|world'))
print(re.search('hello.world', 'hello\nworld', re.S))
