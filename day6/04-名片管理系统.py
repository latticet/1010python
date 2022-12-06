"""
名片管理 系统
# 名片盒子  列表中存放字典,为什么要这样存放?为什么不是字典中存放列表?
cards = [
    {“name”:”张三”,”tel”:”17715154242”,”job”:”CEO”,”addr”:”天府新谷”,”company”:”源码时代”},  # 字典
    {名片信息2},
    {名片信息3}
]
需要完成的功能 就是对 名片盒子 进行增删改查
1. 添加名片: 根据用户录入的信息, 组装成字典 追加到名片盒子里面  cards.append(一个人的名片字典)
2. 显示所有名片: 遍历名片盒子输出名片信息
3. 修改名片:  录入需要修改名片的姓名, 根据名字到名片合子查找对应的哪一张名片,
    如果找到 , 重写录入新的名片信息, 完成修改操作
4. 删除名片: 录入需要删除名片的姓名, 根据名字到名片盒子中查到对应的名片并删除.
"""
cards = [
    {'name': 'hello1', 'tel': '123', 'job': 'ceo'},
    {'name': 'hello2', 'tel': '123', 'job': 'ceo'},
    {'name': 'hello3', 'tel': '123', 'job': 'ceo'}
]

while True:
    # 用户通过序号选择功能
    code = input('选择功能【1添加|2显示|3修改|4删除】：')
    if code == '1':
        # 添加名片
        # 接收用户输入
        name = input('name:')
        tel = input('tel:')
        job = input('job:')
        # 构建字典
        info = {'name': name, 'tel': tel, 'job': job}
        # 添加到列表
        cards.append(info)
        print('添加成功')
    elif code == '2':
        print('姓 名\t手机号\t职位')
        # 遍历列表中的所有字典
        for card in cards:
            for value in card.values():
                print(value, end='\t')
            print()
    elif code == '3':
        # 修改
        # 接收用户名
        name = input('姓名：')
        # 遍历列表
        for card in cards:
            # 根据用户名找到对应的dict
            if card['name'] == name:
                # 接收用户输入
                name = input('name:')
                tel = input('tel:')
                job = input('job:')

                # 设置内容
                card['name'] = name
                card['tel'] = tel
                card['job'] = job
                print('修改成功')
                break
        else:
            print('姓名不存在')
    elif code == '4':
        # 通过姓名删除名片信息
        # 接收要删除的姓名
        name = input('姓名：')
        # 遍历列表
        for card in cards:
            if card['name'] == name:
                cards.remove(card)
                print('删除成功')
                break
        else:
            print('没有要删除的名片')
    elif code == 'quit':
        break
    else:
        print('输入错误')
