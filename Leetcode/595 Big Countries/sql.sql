-- https://leetcode.com/problems/big-countries/
--  schema 
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | name        | varchar |
-- | continent   | varchar |
-- | area        | int     |
-- | population  | int     |
-- | gdp         | int     |
-- +-------------+---------+
-- Find the name, population, and area of the big countries.

SELECT name, population, area 
FROM World
WHERE  area > 300_0000
OR population > 2500_0000





SELECT name, population, area
FROM world
WHERE area > 3000000 OR population >= 25000000

-- or using union 

SELECT name, population, area
FROM world
WHERE area > 3000000   
-- combine the results of 2 or more select statements 
UNION 
SELECT name, population, area
FROM world
WHERE population >= 25000000
