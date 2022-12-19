import time
from datetime import datetime

# TODO datetime类
# # 类方法
# 说明：下面几个类方法，都返回的是datetime对象
# datetime.today()	当前时间，localtime。
"""
datetime_obj = datetime.today()
print(datetime_obj)
print(type(datetime_obj))
"""

# datetime.now()	当前的时间。
"""
print(datetime.now())
"""

# datetime.utcnow()	当前格林时间。
"""
print(datetime.utcnow())
"""

# datetime.fromtimestamp()	将时间戳的转换为时间对象。
"""
timestamp = time.time()
print(datetime.fromtimestamp(timestamp))
"""

# datetime.strptime(str,fmt)	字符串时间按照fmt格式转化为datetime对象
"""
datetime_str = "2023-1-1 10:10:10"
datetime_obj = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
print(datetime_obj)
print(type(datetime_obj))
"""

# # 对象方法
# datetime.date()	返回一个date对象。
"""
datetime_obj = datetime.now()
date_obj = datetime_obj.date()
print(date_obj)
print(type(date_obj))
"""

# datetime.time()	返回time对象。
"""
datetime_obj = datetime.now()
time_obj = datetime_obj.time()
print(time_obj)
print(type(time_obj))
"""

# datetime.strftime(fmt)	按照fmt的格式将datetime时间，转化为字符串时间
datetime_obj = datetime.now()
datetime_str = datetime_obj.strftime('%Y-%d-%m %H%:%M:%S')
print(datetime_str)
print(type(datetime_str))
