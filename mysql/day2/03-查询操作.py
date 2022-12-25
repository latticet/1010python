# TODO 1.导入pymysql
import pymysql

# TODO 2.创建连接对象
# host:主机地址,默认localhost
# port:端口号，默认3306
# user：mysql账号
# password:mysql密码
# database: 指定要操作的数据库
# charset:通信的字符集
conn = pymysql.connect(host='localhost', port=3306,
                       user='root', password='root',
                       database='advanced', charset='utf8')

# TODO 3.获取游标对象
cursor = conn.cursor()

# TODO 4.执行sql语句
# 返回受影响行数
rows = cursor.execute('select * from student')
print(f'受影响行数：{rows}')

# TODO 5.获取结果集
# 说明：游标对象只能获取一次结果集
# 每次获取一条记录
print(cursor.fetchone())
# 获取指定条数: size:记录数
print(cursor.fetchmany(2))
# 一次性获取所有
print(cursor.fetchall())

# TODO 6.关闭游标对象
cursor.close()

# TODO 7.关闭连接对象
conn.close()
