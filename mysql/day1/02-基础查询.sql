-- 查询多个字段
-- SELECT 字段1, 字段2, ... FROM 表名;
SELECT stu_name, stu_no FROM student;

-- 字段设置别名
-- SELECT 字段1 [AS 别名1], 字段2 [AS 别名2] ... FROM 表名;
SELECT stu_name AS name, stu_no AS number FROM student;
-- SELECT 字段1 [ 别名1], 字段2 [ 别名2] ... FROM 表名;
SELECT stu_name name, stu_no number FROM student;

-- 去除重复记录
-- SELECT DISTINCT 字段列表 FROM 表名;
SELECT DISTINCT class_id FROM student;

