# TODO write()
# 说明：一次性写入一个内容
"""
# 打开文件
f = open('resource/demo2.txt', 'w', encoding='utf8')
# w: 覆盖写。文件不存在创建，存在，覆盖原内容
# 操作文件
f.write('hello4')
f.write('hello5')
# 关闭文件
f.close()
"""

# TODO writelines([xx, xx])
# 说明：一次性写入多个内容
f = open('resource/demo3.txt', 'w', encoding='utf8')
f.writelines(['111\n', '222\n', '333\n', '444\n'])
f.close()
