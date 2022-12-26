# 三元运算符（三目运算符）
a = 300
b = 200

if a > b:
    print(a)
else:
    print(b)

print('==' * 20)

# 三元运算符
# 语法：
"""
python:条件成立执行的表达式 if 条件 else 条件不成立执行的表达式

其他语言：条件 ? 条件成立执行的表达式 : 条件不成立执行的表达式
"""

c = a if a > b else b
print(c)

