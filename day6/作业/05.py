"""
按照以下需求，封装一个函数
1.1 设计一个功能从键盘获取用户的姓名、性别、家庭地址
1.2 打印从该功能中获取的信息
"""
def info():
    # 获取输入的信息
    name = input('name:')
    gender = input('gender:')
    addr = input('addr:')

    # 输出到终端
    print(name)
    print(gender)
    print(addr)

info()