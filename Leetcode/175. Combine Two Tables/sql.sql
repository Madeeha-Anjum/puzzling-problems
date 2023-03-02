-- https://leetcode.com/problems/combine-two-tables/
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | personId    | int     |
-- | lastName    | varchar |
-- | firstName   | varchar |
-- +-------------+---------+

-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | addressId   | int     |
-- | personId    | int     |
-- | city        | varchar |
-- | state       | varchar |
-- +-------------+---------+

-- first name, last name, city, and state of each person in the Person table.  



SELECT lastname, firstname, city, state
FROM Person
LEFT JOIN  Address
-- Left Join is used to get all the rows from the left table, even if there are no matches in the right table.
ON Address.personId = Person.personId


 