import re

# 身份证号

# 位数： 18
# 第一位： 1 - 8
# 最后一位: [0-9X]

re_str = '^[1-8][0-9]{16}[0-9X]$'

code = input('身份证号：')
if re.search(re_str, code):
    print('格式正确')
else:
    print('格式错误')
