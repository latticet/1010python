# 输出AAAAAA  -> BAAAA
"""
print('BAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
print('BAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
print('BAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
print('BAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
print('BAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
"""
# 可以给这个数据起个名字 定义变量
# TODO 定义变量
"""
语法：
变量名 = 变量值
=:表示为变量赋值
"""

# TODO 标识符(变量名，函数名，类名)
"""
说明：python中所有带名字的对象，都叫做标识符。变量名，函数名，类名
     在python中变量名一般都使用下划线的命名风格
规范(必须遵循)：
    1. 由字母数字下划线（_）组成,不能以数字开头
    2. 区分大小写
    3. 不能使用python的关键字
风格（不是必须遵循，建议要这样起名字）：
    驼峰命名法：  
        小驼峰：单词组合使用的时候，第一个单词首字母小写，后面的单词首字母大写
            nameError
            helloWorld
        大驼峰：单词组合使用的时候， 所有单词首字母大写
            NameError
            HelloWorld
    下划线命名：单词组合使用的时候, 单词之间用下划线拼接
          name_error
          hello_world
"""


# python的关键字
# python官方使用的一些单词（标识符）
# 查看python中所有的关键字
import keyword

print(keyword.kwlist)

a = 'BAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
print(a)

# 下面单词是否可以作为变量使用
"""
name
nameWord
FirstName
info1
123abc   # 不符合
abc123
_hello
info_Tow
File_Name
if_hello
Hello-Word  # 不符合
"""