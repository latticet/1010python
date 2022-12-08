# 选择功能
code = input('功能选择[1注册2登录]：')
if code == '1':
    # 接收用户信息
    username = input('username:')
    password = input('password:')

    # 将用户信息写入到文件中
    f = open('resource/userinfo.txt', 'a', encoding='utf8')
    f.write(f'{username},{password}\n')
    f.close()
    print(f'【{username}】注册成功')
elif code == '2':
    # 接收用户信息
    username = input('username:')
    password = input('password:')

    # 读取所有用户信息
    f = open('resource/userinfo.txt', 'r', encoding='utf8')
    while True:
        line = f.readline()
        # 去掉每行中的换行
        # '11,11\n' -> '11,11'.split(',')  [user,pass]
        sys_user, sys_pass = line.rstrip('\n').split(',')
        # 判断用户输入和系统中的用户信息是否匹配
        if sys_user == username and sys_pass == password:
            print('登录成功')
            break
        if not line:
            print('登录失败')
            break
else:
    print('功能不存在')
