-- SELECT 字段列表 FROM 表名 WHERE 条件列表;
-- 比较运算符
SELECT * FROM student WHERE stu_id > 3;

-- 逻辑运算符
SELECT * FROM student WHERE stu_id = 6 OR class_id = 1;

-- 模糊查询
SELECT * FROM student WHERE stu_name LIKE '袁_';
SELECT * FROM student WHERE stu_name LIKE '袁%';

-- 范围查询
-- between .. and ..表示在一个连续的范围内查询
-- 查询stu_id 3到5之间的学生信息
SELECT * FROM student WHERE stu_id BETWEEN 3 AND 5;
-- -- 查询stu_id 不是3到5之间的学生信息
SELECT * FROM student WHERE stu_id NOT BETWEEN 3 AND 5;

-- in表示在一个非连续的范围内查询
-- 查询stu_id 2, 4, 5
SELECT * FROM student WHERE stu_id in (2, 4, 5);
-- 查询stu_id 不是2, 4, 5
SELECT * FROM student WHERE not stu_id in (2, 4, 5);

-- is null
-- 查询class_id 是 null的数据
SELECT * FROM student WHERE class_id IS NULL;
-- is not null
-- 查询class_id 不是 null的数据
SELECT * FROM student WHERE class_id IS NOT NULL;