SELECT * FROM training.products;

SELECT AVG(price) FROM training.products;

/* Aggregate function */
SELECT group_name, AVG(price)
FROM training.products
JOIN training.product_groups 
    ON training.products.group_id = training.product_groups.group_id
GROUP BY group_name;

/* Window Function */
SELECT 
    product_name, 
    price, 
    group_name, 
    AVG(price) OVER (PARTITION BY group_name)
FROM training.products
JOIN training.product_groups
    ON training.products.group_id = training.product_groups.group_id
ORDER BY group_name, price DESC;

/* ROW NUMBER */
SELECT
	product_name,
	group_name,
	price,
	ROW_NUMBER () OVER (
		PARTITION BY group_name
		ORDER BY
			price DESC
	)
FROM
	training.products
INNER JOIN training.product_groups USING (group_id);


/* RANK */
SELECT
	product_name,
	group_name,
    price,
	RANK () OVER (
		PARTITION BY group_name
		ORDER BY
			price
	)
FROM
	training.products
INNER JOIN training.product_groups USING (group_id);


/* RANK without partitioning */
SELECT product_name, price, RANK() OVER (ORDER BY price)
FROM training.products;


/* FIRST VAULE */
SELECT
	product_name,
	group_name,
	price,
	FIRST_VALUE (price) OVER (
		PARTITION BY group_name
		ORDER BY
			price
	) AS lowest_price_per_group
FROM
	products
INNER JOIN product_groups USING (group_id);

/* LAST VALUE */
SELECT
	product_name,
	group_name,
	price,
	LAST_VALUE (price) OVER (
		PARTITION BY group_name
		ORDER BY
			price RANGE BETWEEN UNBOUNDED PRECEDING
		AND UNBOUNDED FOLLOWING
	) AS highest_price_per_group
FROM
	products
INNER JOIN product_groups USING (group_id);


/* LAG */
SELECT
	product_name,
	group_name,
	price,
	LAG (price, 1) OVER (
		PARTITION BY group_name
		ORDER BY
			price
	) AS prev_price,
	price - LAG (price, 1) OVER (
		PARTITION BY group_name
		ORDER BY
			price
	) AS cur_prev_diff
FROM
	products
INNER JOIN product_groups USING (group_id);


/* LEAD */
SELECT
	product_name,
	group_name,
	price,
	LEAD (price, 1) OVER (
		PARTITION BY group_name
		ORDER BY
			price
	) AS next_price,
	price - LEAD (price, 1) OVER (
		PARTITION BY group_name
		ORDER BY
			price
	) AS cur_next_diff
FROM
	products
INNER JOIN product_groups USING (group_id);