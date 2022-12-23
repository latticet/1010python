-- SELECT 字段列表 FROM 表名 GROUP BY 分组字段名
-- 以class_id进行分组
SELECT class_id FROM student GROUP BY class_id;

-- 聚合函数配合分组使用
-- 查询每个班级的总人数
SELECT class_id, count(*) total_student FROM student GROUP BY class_id;

-- 查询每个班中最大的年龄
SELECT class_id, MAX(stu_age) FROM student GROUP BY class_id;

-- 查询每个班中最小的年龄
SELECT class_id, MIN(stu_age) FROM student GROUP BY class_id;

-- 查询每个班级的平均年龄
SELECT class_id, AVG(stu_age) FROM student GROUP BY class_id;

-- GROUP_CONCAT(expr) 配合分组使用
-- 在分组后，用来聚合其他非分组字段
-- 查询每个班级的学生姓名
SELECT class_id, GROUP_CONCAT(stu_name) FROM student GROUP BY class_id;

-- HAVING配合分组使用，不能单独使用
-- 对分组之后的数据进行过滤
-- 查询人数大于3的班级
SELECT class_id FROM student GROUP BY class_id HAVING COUNT(*) > 3;

-- 平均年龄大于30的班级
SELECT class_id FROM student GROUP BY class_id HAVING AVG(stu_age) >30;

-- where 和 group by同时使用
-- 查询每个班年龄大于20的所有同学姓名
SELECT class_id, GROUP_CONCAT(stu_name) FROM student
WHERE stu_age > 20
GROUP BY class_id;
