import re

# 需求
# 判断用户输入的是否是一个python模块
# 接收用户输入
filename = input('文件名：')
# xx.py   字母数字下划线组成，不能以数字开头

if re.search('^[a-z_]\w{0,7}\.py$', filename):
    print('符合模块规范')
else:
    print('不符合模块规范')
