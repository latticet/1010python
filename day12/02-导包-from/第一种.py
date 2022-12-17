# 语法： from 包[.包.n] import 模块1 [as 别名], 模块2 [as 别名], ...
from package1 import module2, module1
from package2.package_a import module_a1 as a1, module_a2 as a2
from package2.package_b import module_b1, module_b2

print(module1.name)
print(module2.name)

print('==' * 20)

print(a1.name)
print(a2.name)

print('==' * 20)

print(module_b2.name)
print(module_b1.name)
