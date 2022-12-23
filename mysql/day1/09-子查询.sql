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

