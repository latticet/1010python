import pymysql

# 需求：通过学生姓名查询学生信息
# 接收用户输入
name = input('学生姓名：')

conn = pymysql.connect(user='root', password='root', database='advanced', charset='utf8')
cursor = conn.cursor()
# 执行sql语句
# TODO sql注入问题
sql = f'select * from student where stu_name = "{name}"'
# select * from student where stu_name = "" or 1 = 1 or ""
rows = cursor.execute(sql)
# 获取结果集
print(cursor.fetchall())

# 关闭
cursor.close()
conn.close()
