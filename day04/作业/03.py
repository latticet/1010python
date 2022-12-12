"""
使用while循环输出2000年到2100年之间的闰年
闰年：400的倍数  或者   是4的倍数不是100的倍数
"""
year = 2000
while year <= 2100:
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print(year)
    year += 1