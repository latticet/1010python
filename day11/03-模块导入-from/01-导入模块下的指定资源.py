# 语法：from 模块名 import 资源名1 [as 别名], 资源名2, ...
from module1 import name as m1_name, fn, Demo
from module2 import name as m2_name

name = 'myname'

print(m1_name)
print(m2_name)

print(name)
fn()
print(Demo())
