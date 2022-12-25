# 1. 导入pymysql
import pymysql

# 2. 创建连接对象
conn = pymysql.connect(user='root', password='root', database='advanced', charset='utf8')

# 3. 获取游标对象
# 元组游标：cursor=pymysql.cursors.Cursor  【默认】
# 字典游标：cursor=pymysql.cursors.DictCursor
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# 4. 执行sql语句
sql = 'select * from student'
rows = cursor.execute(sql)
print(rows)

# 5. 获取结果集
print(cursor.fetchone())
print(cursor.fetchall())

# 6. 关闭游标对象
cursor.close()
# 7. 关闭连接对象
conn.close()
