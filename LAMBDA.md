```python
"""
Lambda function input(prompt)
 
"""
#  lambda function examples 

# returns the sum of all the numbers in the list
res = lambda x: x + 1
print(res(num)) # we have to call out lambda function 

# the lambda function is used to filter the list of numbers
# the lambda function runs on each element of the list  and returns i+1
lst = [square(i) for i in [1, 2, 3, 4, 5]]
res = [lambda i: i + 1 for i in [1, 2, 3, 4, 5]]
# instead of a for loop we can use a list and map
res = list(map(lambda i: i + 1, [1, 2, 3, 4, 5]))


# filter() function takes a function and a list | returns a subsetted list of the elements where the function returns true.

res = list(filter(lambda x: x % 2 == 0, xs))

# true and false with lambda
lambda x: True if x % 2 == 0 else False


 
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Python built in functions take a key argument which is the element to be operated on from nums list.
# the key is what is used to compare 
sort_lambda = sorted(nums, key = lambda x: x%2)
print(sort_lambda)
```