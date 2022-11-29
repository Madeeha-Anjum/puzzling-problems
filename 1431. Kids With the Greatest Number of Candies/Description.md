# Kids With the Greatest Number of Candies

Input = array of candies, the values represent the number of candies that a kid has
extra-candies = integer that represents how many extra candies there are 


- So we want to find out if we distribute the extra candies will the 
so that the current kid `[candies[i]]` has the most candies out of all the kids in the array candies.
- note that more than one kid can have the most candies 


Example:

Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true]
Explanation 

Kid 1 has 2 candies and if he or she receives all extra candies (3) will have 5 candies --- the greatest number of candies among the kids. 
Kid 2 has 3 candies and if he or she receives at least 2 extra candies will have the greatest number of candies among the kids. 
Kid 3 has 5 candies and this is already the greatest number of candies among the kids. 
Kid 4 has 1 candy and even if he or she receives all extra candies will only have 4 candies. 
Kid 5 has 3 candies and if he or she receives at least 2 extra candies will have the greatest number of candies among the kids. 