-- sql语句默认查询出来的数据，按照主键字段的升序排序
-- 升序：从小到大
-- 降序：从大到小

-- 查询学生信息，年龄从小到大排序
SELECT * FROM student ORDER BY stu_age ASC;
SELECT * FROM student ORDER BY stu_age;

-- 查询学生信息，年龄从大到小排序
SELECT * FROM student ORDER BY stu_age DESC;

-- 查询学生信息，年龄从大到小排序，stu_id从大到小
SELECT * FROM student ORDER BY stu_age DESC, stu_id DESC;


