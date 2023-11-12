Table: Weather

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| recordDate    | date    |
| temperature   | int     |
+---------------+---------+
id is the column with unique values for this table.
This table contains information about the temperature on a certain day.

Write a solution to find all dates' Id with higher temperatures compared to its previous dates (yesterday).'

Return the result table any order.

Okay try your best to get this one.  


-- difference in days between 2 dates
SELECT DATEDIFF(day, '2017/08/25', '2011/08/25') AS DateDiff;


-- Join on it self where ever the difference of data is 1 
SELECT T1.id, T1.recordDate
FROM Weather T1, Weather T2
WHERE DATEDIFF(T1.recordDate, T2.recordDate) = 1 
AND T1.temperature > T2.temperature   

