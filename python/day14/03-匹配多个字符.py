import re

# TODO * 匹配前一个字符出现0次或者无限次 {0,}
print(re.search('ha*', 'h').group())
print(re.search('ha*', 'ha').group())
print(re.search('ha*', 'haa').group())
print('--' * 20)

# TODO + 匹配前一个字符出现1次或者无限次 {1,}
print(re.search('ha+', 'h'))  # 匹配不到
print(re.search('ha+', 'ha'))
print(re.search('ha+', 'haa'))
print('--' * 20)

# TODO ? 匹配前一个字符出现1次或者0次 {0,1}
print(re.search('ha?', 'h'))
print(re.search('ha?', 'ha'))
print(re.search('ha?', 'haa'))
print('--' * 20)

# TODO {m} 匹配前一个字符出现m次
print(re.search('eg{2}', 'egg').group())
print(re.search('eg{2}', 'eg'))
print('--' * 20)

# TODO {m,n} 匹配前一个字符出现从m到n次
print(re.search('a{1,3}', 'a').group())
print(re.search('a{1,3}', 'aa').group())
print(re.search('a{1,3}', 'aaa').group())
print(re.search('a{1,3}', 'aaaa').group())
print('--' * 20)

# TODO {m,}	匹配前一个字符至少出现m次
print(re.search('a{2,}', 'aa').group())
print(re.search('a{2,}', 'aaa').group())
print(re.search('a{2,}', 'aaaa').group())