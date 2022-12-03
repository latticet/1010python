
t1 = ('python', 'mysql', 'linux')
# 元组拆包：将元组中的元素依次赋值给前面的变量。
# 注意：变量数量和元素数量必须保持一致
# 说明：一般在业务场景中主要使用到元组拆包
a, b, c = t1
print(a, b, c)

# 字符串拆包
a1, a2, a3 = 'abc'
print(a1, a2, a3)

# 列表拆包
x, y = [100, 200]
print(x, y)

# 变量格式化
print('姓名:%s，年龄:%d' % ('hello', 18))