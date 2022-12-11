"""
类名：CardsManager
方法：
    __init__:
        cards = [{},{},{}]
    add_card
    show_cards
    edit_card
    del_card
    run
"""


class CardsManager:
    def __init__(self):
        self.cards = [
            {'name': 'hello1', 'tel': '123', 'job': 'ceo'},
            {'name': 'hello2', 'tel': '123', 'job': 'ceo'},
            {'name': 'hello3', 'tel': '123', 'job': 'ceo'}
        ]

    def add_card(self):
        """添加名片"""
        # 接收用户输入
        name = input('name:')
        tel = input('tel:')
        job = input('job:')
        # 构建字典
        info = {'name': name, 'tel': tel, 'job': job}
        # 添加到列表
        self.cards.append(info)
        print('添加成功')

    def show_cards(self):
        """查看所有名片"""
        print('姓 名\t手机号\t职位')
        # 遍历列表中的所有字典
        for card in self.cards:
            for value in card.values():
                print(value, end='\t')
            print()

    def edit_card(self):
        """修改名片"""
        # 修改
        # 接收用户名
        name = input('姓名：')
        # 遍历列表
        for card in self.cards:
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

    def del_card(self):
        """删除名片"""
        # 接收要删除的姓名
        name = input('姓名：')
        # 遍历列表
        for card in self.cards:
            if card['name'] == name:
                self.cards.remove(card)
                print('删除成功')
                break
        else:
            print('没有要删除的名片')

    def run(self):
        while True:
            # 用户通过序号选择功能
            code = input('选择功能【1添加|2显示|3修改|4删除】：')
            if code == '1':
                self.add_card()
            elif code == '2':
                self.show_cards()
            elif code == '3':
                self.edit_card()
            elif code == '4':
                self.del_card()
            elif code == 'quit':
                break
            else:
                print('输入错误')


cards = CardsManager()
cards.run()
