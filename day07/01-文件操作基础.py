# TODO 1. 打开文件
# 语法: f = open('文件路径'[, mode='r'], encoding='utf8')
# 参数：
# -- mode: 打开模式，默认值：r 。 r:read w:write a:append
# -- encoding: 字符集
# 返回：资源句柄
# 绝对路径：根路径找到对应的资源
# r'':让字符成为原生字符
"""
file_path = r'F:\20221010软件测试精英班\09 python阶段\1010python\day7\resource\demo1.txt'
f = open(file_path, mode='r', encoding='utf8')
"""
# 相对路径：以当前执行脚本所在目录作为参照物，查找对应的资源
f = open('resource/demo1.txt', encoding='utf8')

# TODO 2. 操作文件
# f.read() 读取所有内容
content = f.read()
print(content)

# TODO 3. 关闭文件
# f.close()
f.close()
