# 语法：
# from 包[.包.n].模块 import 资源1 [as 别名], 资源2 [as 别名], ...
from package1.module1 import name as m1_name
# 导入module_b1下面的name
from package2.package_b.module_b1 import name


print(name)

print(m1_name)
