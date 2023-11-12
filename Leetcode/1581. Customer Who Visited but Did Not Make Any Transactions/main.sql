Table: Visits

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| visit_id    | int     |
| customer_id | int     |
+-------------+---------+
visit_id is the column with unique values  

Table: Transactions

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| transaction_id | int     |
| visit_id       | int     |
| amount         | int     |
+----------------+---------+
transaction_id is column with unique

Write a solution to find the IDs of the users who visited without making any transactions and the number of times they made these types of visits.

Return the result table sorted in any order.



SELECT customer_id 
FROM Visits
INNER JOIN Transactions 
ON Visits.visit_id = Transactions.visit_id


-- users that made transaction 
SELECT customer_id 
FROM Visits
RIGHT JOIN Transactions
ON Visits.visit_id = Transactions.visit_id

 

-- users that did not make transactions 
SELECT customer_id, Count(visit_id)
FROM Visits
WHERE visit_id  NOT IN (
   SELECT visit_id  
    FROM Transactions
)





