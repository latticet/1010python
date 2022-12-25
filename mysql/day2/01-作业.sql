-- A. 查询卖的最贵的商品的名称    
-- 1. 获取商品的最高价格
SELECT MAX(shop_price) FROM ecs_goods;
SELECT goods_name, shop_price FROM ecs_goods 
ORDER BY shop_price DESC;
-- 2. 通过最高价格获取对应商品
SELECT goods_name FROM ecs_goods WHERE shop_price = 3010;
-- 子查询
SELECT goods_name FROM ecs_goods WHERE 
shop_price = (SELECT MAX(shop_price) FROM ecs_goods);

-- B. 查询商品品牌为”仓品”的 所有商品名称和商品价格
-- 1. 通过品牌名称获取品牌id
SELECT brand_id FROM ecs_brand WHERE brand_name = '仓品';
-- 2. 通过品牌id获取商品信息
SELECT goods_name, shop_price FROM ecs_goods
WHERE brand_id = 15;
-- 子查询
SELECT goods_name, shop_price FROM ecs_goods
WHERE brand_id = (SELECT brand_id FROM ecs_brand WHERE brand_name = '仓品');

-- C. 查询商品品牌为”仓品”的 所有商品名称和商品价格 按照价格降序排列
SELECT goods_name, shop_price FROM ecs_goods
WHERE brand_id = (SELECT brand_id FROM ecs_brand WHERE brand_name = '仓品') ORDER BY shop_price DESC;

-- D1. 查询每个商品品牌（品牌id）的商品数量
SELECT brand_id,count(*) FROM ecs_goods 
GROUP BY brand_id;

-- D2. 查询每个商品品牌(品牌名称)的商品数量
-- goods g, brand b
-- goods:0 1 22
-- brand:  飞利浦 仓品
-- 第一种
SELECT b.brand_name,count(g.goods_id) FROM ecs_goods g
INNER JOIN ecs_brand b ON g.brand_id = b.brand_id 
GROUP BY g.brand_id

-- 第二种
SELECT b.brand_name,count(g.goods_id) FROM 
ecs_goods g,ecs_brand b
WHERE g.brand_id = b.brand_id
GROUP BY b.brand_id;

-- 查询商品品牌对应的商品数量大于5的商品品牌名称
-- 获取商品数量大于5的品牌id
-- 品牌对应的商品种类数量
SELECT brand_id, count(*) FROM ecs_goods GROUP BY brand_id
HAVING count(*) > 5;

-- goods g, brand b
SELECT b.brand_name, count(g.goods_id) FROM 
ecs_goods g, ecs_brand b
WHERE g.brand_id = b.brand_id
GROUP BY g.brand_id
HAVING count(g.goods_id) > 5;


-- 品牌对应的商品库存数量
SELECT b.brand_name, SUM(g.goods_number) FROM 
ecs_goods g, ecs_brand b
WHERE g.brand_id = b.brand_id
GROUP BY g.brand_id
HAVING SUM(g.goods_number) > 5;






