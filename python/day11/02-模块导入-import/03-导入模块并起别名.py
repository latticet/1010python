# 导入模块并起别名
# 语法：import 模块名1 [as 模块1别名], 模块名2 [as 模块2别名,] ...

import module1 as m1, module2

# 起别名作用：
"""
1. 简化模块名
2. 解决冲突
"""

module1 = 100

print(module1)
print(m1.name)
