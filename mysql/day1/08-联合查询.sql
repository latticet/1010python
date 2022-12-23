/*
SELECT 字段列表 FROM 表A ... 
UNION [ ALL ]
SELECT 字段列表 FROM 表B ....;
*/
-- UNION ALL -- 不去重
SELECT * FROM student WHERE stu_age > 30
union all
SELECT * FROM student WHERE stu_age < 30;


SELECT stu_age FROM student WHERE stu_age > 30
union all
SELECT stu_age FROM student WHERE stu_age < 30;

-- UNION 去重
-- 只留下一个字段
SELECT stu_age FROM student WHERE stu_age > 30
union
SELECT stu_age FROM student WHERE stu_age < 30;
