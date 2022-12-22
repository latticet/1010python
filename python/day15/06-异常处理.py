# BaseException
    # Exception
        # Zero
        # Name
        # Value

# 异常处理语法
# 异常语句执行流程
"""
try:
    可能发生异常的代码
except 异常类型 as e:
    捕获到异常执行的代码块
else:
    没有异常执行的代码块
finally:
   是否有异常都要执行的代码块
"""

# 异常特点
# 异常会向外抛
# try异常语句可以嵌套

# 自定义异常
"""
class XXError(Exception):
     def __str__(self):
        return '异常描述信息'
"""

# 自定义异常抛出
# raise XXError()