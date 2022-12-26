import pymysql

# 需求：通过学生姓名查询学生信息
# 接收用户输入
name = input('学生姓名：')
age = int(input('学生年龄：'))

conn = pymysql.connect(user='root', password='root', database='advanced', charset='utf8')
cursor = conn.cursor()
# 执行sql语句
# TODO sql注入解决
# 在用户输入数据的地方，全部用占位符代替
# 注意：占位符统一使用%s, 占位符不用引号包裹
sql = 'select * from student where stu_name = %s or stu_age = %s'
# select * from student where stu_name = "" or 1 = 1 or ""
rows = cursor.execute(sql, args=[name, age])
# 获取结果集
print(cursor.fetchall())

# 关闭
cursor.close()
conn.close()
