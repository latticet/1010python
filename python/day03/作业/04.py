"""
火车站安检
需求：
1）.  定义变量has_ticket表示是否有车票。
2）.  定义变量knife_length表示刀的长度，单位：厘⽶。
3）.⾸先通过安检，检查刀的长度是否大于20cm。
	l 如果小于等于20cm，前往检票，提示“安检通过，请前往检票！”。
	l 如果大于20cm，不允许进入检票，提示“警告！携带刀的长度为：XXXcm，大于20cm，请退出！”
4）.  检票时，判断是否有车票。
	l 如果有车票允许上车。提示“通过，请上车！”。
	l 如果没有车票不允许上车，提示“检票失败，不通过！”。
"""

# 定义变量
has_ticket = int(input('是否有票：[0:No|1:Yes]'))
knife_length = int(input('knife：'))

# 执行流程
# 判断knife合理性
if knife_length <= 20:
    print('安检通过，请前往检票！')
    if has_ticket:
        print('通过，请上车！')
    else:
        print('检票失败，不通过！')
else:
    print(f'警告！携带刀的长度为：{knife_length}cm，大于20cm，请退出！')
