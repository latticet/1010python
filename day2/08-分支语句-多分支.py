# 语法
"""
if 条件表达式1:
    条件1成立执行的代码块
elif 条件表达式2:
    条件2成立执行的代码块
elif 条件表达式n:
    条件n成立执行的代码块
else:
    上面条件都不成立执行的代码块
"""
# 执行流程

# 需求：
"""
分数：
90以上优秀
80以上良好
70以上一般
60以上及格
其他：下个班见
"""
score = int(input('分数：'))
if score >= 90:
    print('优秀')
elif score >= 80:
    print('良好')
elif score >= 70:
    print('一般')
elif score >= 60:
    print('及格')
else:
    print('下个班警告')
