# else
# 当循环正常结束，执行else代码块中的内容。如果循环是break结束的就不执行else的内容。

# while
i = 0
while i < 3:
    print(i)
    i += 1
else:
    print('循环结束')

print('--' * 20)

i = 0
while i < 3:
    print(i)
    i += 1
    break
else:
    print('循环结束')
print('==' * 20)

# for
for item in [1, 2]:
    print(item)
else:
    print('循环结束')

print('--' * 20)

for item in [1, 2]:
    print(item)
    break
else:
    print('循环结束')
