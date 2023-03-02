<!-- 
Hash Functions, Collisions, Time Complexity of HashMap operations such as insert, delete, and search
  - How are HashMaps different from Sets and Arrays? When would you use a HashMap over a Set or Array?  - 
 -->
# Properties of a Hashmap

- hashmap is not ordered
- keys are unique
- O(1) time for insertion
- Also called: python : dict, java: map, JavaScript: object

# components of a hashmap

1. Array -> stores the values
2. Hash function -> maps the keys to the array
3. colision resolution -> handles collisions

# Example of a hashmap

beans -> 1.8
corn -> 1.3
Rice -> 1.5

---

```bash
This is out hash map: 
 _______________________
|_____|_____|_____|_____|
   1     2     3     4  
```

Now we want to add("beans", 1.8) to the hashmap

How do we do this?

We need some way to turn "beans" into an index in the array so we know where to put it

This is where the hash function comes in

```bash
# here we use a simple hash function but this can be very complex
Hash function: 
index = len(key) - 1

```

Now we have placed "beans" in the array at index 4

```bash
# This is our new hash map: 
 ___________________________________
|                   |["beans", 1.8)]|
|_____|_____|_______|_______________|
   1     2      3          4  
```

Now we want to get("beans")

How do we do this?

The  get function calls the hash function to get the index of the array

We get the value "1.8" at index 4

___

## Collision Example

```bash
# This is our new hash map: 
 ____________________________________________
|            ["Corn", 2.38)] |["beans", 1.8)]|
|_____|_____|________________|_______________|
   1     2            3                  4  
```

Now we want to add("Rice", 1.5) to the hashmap

How do we do this?

Put "Rice" into the hash function

```bash
#   the has function is the same as before
index = len(key) - 1

```

we get index 3

But we already have a value at index 3

What do we do? oh nooo "COLLISION"

```bash
# This is our new hash map: 
# Each cell with use a list to store the pairs in
 ____________________________________________
|            ["Corn", 2.38)] |["beans", 1.8)]|
|_____|_____|["Rice", 1.92)]|_______________|
   1     2            3                  4  
```

Now we want to get("Rice")

what happens?

get will call the hash function to get the index  

```bash
#   the has function is the same as before
index = len(key) - 1

```

we get index 3

Now we have to search the list at index 3 for the  key "Rice" and return the value "1.92"

## Performance of hashmap

- depends on how many items are in each cell of the array
- so its better to only have one item in the cell

But think !

If we had a better has function we could have avoided the collision!!!!! :fire:

For example:

```bash
index = sum(ASCII values of each character in the key) 
% len(array) 
OR 5 in our case
```

## :fire: Refer to the code for more details

## HashMap vs Set vs Array & searching  complexity

sets -> store unique values -> O(1) time for searching because it is a hashset
Arrays -> store values -> O(n) time for searching
HashMap -> store key value pairs ->  O(1) time for searching

## When would you use a HashMap over a Set or Array?

sets -> store unique values
Arrays -> store values by a specific order
HashMap -> store key value pairs
