# 第一级别
"""
python内置包模块目录
"""
# 第二级别
"""
sys.path = [
  当前目录,
  系统标准包模块目录,
  第三方包模块目录
]
"""

import sys
from pprint import pprint

pprint(sys.path)

# python安装好以后得包或者模块
# 内置  builtin
# 标准的


# 说明：
# 我们在自定义包或者模块的时候，不要起和系统或者第三方同名的包模块名字。
