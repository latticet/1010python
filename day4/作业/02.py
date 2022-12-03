"""
求解1-100 能被3和5同时整除的数字的和
"""
total = 0
i = 1
while i < 101:
    if i % 3 == 0 and i % 5 == 0:
        total += i
    i += 1

print(total)