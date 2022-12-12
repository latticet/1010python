"""
python编写一个聊天记录保存功能，不断获取用户输入信息，保存到record.log文件
"""
f = open('record.log', 'w', encoding='utf8')
while True:
    msg = input('信息：')
    if msg == 'quit':
        break
    f.write(msg+'\n')

f.close()
