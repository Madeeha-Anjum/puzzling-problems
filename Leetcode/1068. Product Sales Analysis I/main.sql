Table: Sales

+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| sale_id     | int   |
| product_id  | int   |
| year        | int   |
| quantity    | int   |
| price       | int   |
+-------------+-------+
(sale_id, year) is the primary key

Table: Product

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| product_id   | int     |
| product_name | varchar |
+--------------+---------+
product_id is the primary key


Write a solution to report the product_name, year, and price for each sale_id in the Sales table.


-- table of all the products and there price (all in the left that are in the right and all in the left even if there not in the right)
SELECT product_name, year, price
FROM Sales
LEFT JOIN Product
ON Product.product_id = Sales.product_id


