# 循环
# 重复的执行

# while循环语句
# TODO 语法
# 条件表达式的结果True|False
"""
while 条件表达式:
    代码块（循环体）
"""
# TODO 执行流程
"""
# 条件为True
1. 就进入到循环体中执行代码
2. 循环体中代码执行完毕，继续回到while条件表达式执行，如果为True，在进入循环体
3. 直到条件表达式为False，跳过循环循环体继续向下运行
# 条件为False
1. 如果表达式结果为False，那么就跳过循环体，继续向下执行
"""
# 需求：输出3次a变量
a = 'BAAAAAAAAAAAAAAAAAAAAAAAAAA'
# 一般在使用while循环的时候，为了循环次数，会设置一个计数器（控制循环次数的一个变量）
# 计数器
i = 1
while i <= 3:
    print(a)
    i += 1
