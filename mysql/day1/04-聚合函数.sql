-- count 查询记录数量
SELECT COUNT(*) FROM student;
SELECT COUNT(class_id) FROM student;

-- sum 查询字段的总和
SELECT SUM(class_id) FROM student;

-- max 查询字段的最大值
-- 查询最大年龄
SELECT MAX(stu_age) FROM student;

-- min 查询字段的最小值
-- 查询最小年龄
SELECT MIN(stu_age) FROM student;

-- avg 查询字段的平均值
-- 查询平均年龄
SELECT AVG(stu_age) FROM student;