import random


def random_name(count=3):
    name_list = ['贺倩', '杨俊伟', '高博', '敬扬懿', '刘杨', '王木鑫', '袁琳', '文唯', '刘毅杰', '毛佳', '张宇城', '潘春帆', '蒋望舒', '钟伟杰', '孙曹人']
    for i in range(count):
        random.shuffle(name_list)

    name_list_a = random.sample(name_list, 8)
    print(name_list_a)

    for name_a in name_list_a:
        name_list.remove(name_a)

    print(name_list)


if __name__ == '__main__':
    random_name()
