"""
开发敏感词语过滤程序，提示用户输入内容，
如果用户输入的内容中包含特殊的字符：
如 "python"等，将内容替换为 *
"""
# 敏感词
words = ['python', 'mysql', 'linux']

# 用户输入
msg = input('用户输入信息：')
for word in words:
    msg = msg.replace(word, "*" * len(word))
print(msg)
