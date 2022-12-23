-- 标量子查询
-- 子查询语句返回单个值，单行单列
-- 查询1班的所有学生信息
-- a. 利用1班的名称，查询1班的class_id
SELECT class_id FROM class WHERE class_name = '1班';
-- b. 利用class_id查询对应的学生信息
SELECT * FROM student WHERE class_id = 1;
-- 子查询
SELECT * FROM student WHERE class_id = 
(SELECT class_id FROM class WHERE class_name = '1班');
-- -- 查询2班的所有学生信息
SELECT * FROM student WHERE class_id = 
(SELECT class_id FROM class WHERE class_name = '2班');

-- 列子查询
-- 子查询的结果是1列
-- 查询1班和2班所有学生信息
-- a. 通过班级名称，查询班级id
SELECT class_id FROM class WHERE class_name = '1班' 
or class_name = '2班';
-- SELECT class_id FROM class WHERE class_name in ('1班', '2班');
-- b. 通过班级id，查询学生信息
SELECT * FROM student WHERE class_id = 1 OR class_id = 2;
SELECT * FROM student WHERE class_id in(1, 2);
-- 子查询
SELECT * FROM student WHERE class_id 
in (SELECT class_id FROM class WHERE class_name = '1班' 
or class_name = '2班')

-- 行子查询（子查询结果为一行）
-- 查询class_id=1这个班级最大的人,年龄最大的人
-- a. 查询class_id=1这个班最大的年龄
SELECT class_id, max(stu_age) FROM student WHERE class_id = 1;
-- b. 根据年龄和班级id查询学生信息
SELECT * FROM student WHERE class_id = 1 and stu_age = 21;
-- 子查询语句
SELECT * FROM student WHERE (class_id ,stu_age) =
(SELECT class_id, max(stu_age) FROM student WHERE class_id = 1);

-- 表子查询（子查询结果为多行多列）
-- a. 查询分数大于39的所有学生信息
SELECT * FROM student WHERE stu_score > 39;
-- b. 在分数大于39的学生里找出年龄小于30的学生信息
SELECT * FROM
(SELECT * FROM student WHERE stu_score > 39) student_score_gt_39
WHERE stu_age < 30;