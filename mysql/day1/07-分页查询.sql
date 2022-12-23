-- SELECT 字段列表 FROM 表名 LIMIT 起始索引, 查询记录数;
-- 结果集的索引是从0开始的
-- limit 0, 2
SELECT * FROM student LIMIT 0, 2;
-- limit 2, 3
SELECT * FROM student LIMIT 2, 3;

-- 分页原理
-- 确定：当前是第几页， 每页显示多少条（2）
-- 1   limit 0, 2
-- 2   limit 2, 2
-- 3   limit 4, 2
-- 4   limit 6, 2
-- 5   limit 8, 2
-- N   limit (N-1)* 每页条数， 每页条数