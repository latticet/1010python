"""
语法：
input('输入描述信息')
作用：
在终端接收用户的输入,函数返回输入的内容
特点：
1. 阻塞程序继续向下运行，等待用户输入
2. input不管输入什么，返回的都是字符串数据类型
使用：
输入内容，回车
"""
# 接受用户的输入，返回
name = input('学生姓名：')
print(name)
age = input('学生年龄：')
print(age)
print('==' * 20)

# 查看input返回内容的数据类型
print(type(name))
print(type(age))
print('==' * 20)

# 将字符串数字（字符串中包裹着数字'） 转化为数字
str1 = '123'
print(type(str1))
num1 = int(str1)
print(type(num1))

