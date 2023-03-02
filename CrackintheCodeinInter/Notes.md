
# Book Notes

## What the interviewer is thinking/wants

- [ ] enthusiasm in how you discuss your prior experience and how you discuss the team's challenges.They want to see that you will be eager to face the job's challenges.
- [ ] 2 types of interviews. Interview with the company as a whose and interview with a team at the company
- [ ] SOme companies like the entrupunuers spirit where you build something fast
- [ ] 3 types of intervoes(jedi, ninja, priite= behavior, coding, design)
- [ ] Student donst get expereince in software arcatecture,
- [ ] A PM question they want to see when faced with an ambiguous situation, you don't get overwhelmed and stall. They want to see you tackle the problem head on: seeking new information, prioritizing the most important parts, and solving the problem in a structured way.
- [ ] As a PM: type of person who puts himself in the customer's shoes and tries to understand how they want to use the product
- [ ] As a Pm: Your interviewer will want to see that you possess this flexibility in your communication so they as questions such as explain this to your grandmother. oR how you explain your prior projects
- [ ] How to show passion: your interviewers will look for enthusiasm in how you discuss your prior experience and how you discuss the team's challenges.They want to see that you will be eager to face the job's challenges.
- [ ] "Teamwork assessment" - [ ] "Tel! me about a time when a teammate wasn't pulling his / her own weight."Your interviewer is looking to see that you handle conflicts well, that you take initiative, that you understand people, and that people like working with you.

## startups want

- [ ] Startups: entrepreneurial environment. Your resume should ideally show initiative. What sort of projects have you started?

## Interview Behavior formatting answers

- [ ] Interview(Personality, skill, Experience)-  Startups ask allot about your experience, the personality is tested by how you behave with the interviewer, and the skills are assessed by a language test.
- [ ] A behavior question:  question about a challenging situation, and they tell you about a difficult situation their - [ ] they want to know in detail your contribution
- [ ] 4 types of questions companies ask: sanity, Quality, Specialist, Proxy) - easy, challenging, specific, specialized
- [ ] Before the interview:
- [ ] For each role, try to discuss your accomplishments with the following approach:"Accomplished X by implementing Y which led to Z." Here's an example:
- [ ] Use the interview preparation grid to be able to talk about 1 or 2 of the projects you worked on
- [ ] KNOW YOUR TECHNICAL PROJECTS: has a challenging component(more than just learning), you played a central role, you can talk in technical depth, tradeoffs, things you would do differently, scaling.
- [ ] if something was challenging  don't say i did all the hard parts" describe what you did that were challenging
- [ ] Tell me about a time -   Give structured answers and a nugget like: sure let me tell you about the time I did this to let ppl do this. Initially... -   makes the story more clear
- [ ] SAR: situate, Action, Result, -  > Focus on a clear action and use a nugget.
- [ ] love people who build something for fun

## BIG O ( describe the efficiency of algorithms)

**Big O**:

- used to describe efficiency of algorithms aka the run time
- Upper bound on time
- Example: for loop is O(N) since it goes through the whole list once
- **Drop the constants** and non-dominant terms in BigO notation
  - On(N^J) is not always better than O(N)
- **Drop the Non-Dominant Terms** in BigO notation

- When to add or multiply the run times:
  - for each is Multiply
  - this then this is add
- AMORTIZED TIME > worst case happens once in a while
- **Log N** SORTING is the number of times you can divide N by 2 before you get 1 || Cut the problem space in half
- **N Log N** SORTING is the number of times you can divide N by 2 before you get 1 || Cut the problem space in half and **put it together**
-
  - Example: Binary Search | O(Log N) -> searching
  - Example: Merge Sort | O(N Log N) -> sorting
  - Example: Quick Sort | O(N Log N) -> sorting
  - Example: Hash Tables
  - Example: Breadth First Search
  - Example: Depth First Search
  - Example: Dijkstra's Algorithm
  - Example: Divide and Conquer
**Big0 Space**:
- amount of memory or space an algorithm uses
- Example:array of size N takes up N space in memory aka O(N)
- recursive **call** take up space on the stack aka O(N) calls
- Runtime of recursive **calls** often looks like **O(branches^depth)**

  ```py
    # At any given time there is only one function call on the stack meaning there is only one depth meaning its O(N)
    def f(n: int):    
      if (n <= 1):  
          return 1; 
      return f(n - 1) + f(n - 1); 
     

    for i in range(10): # 10s112ms
        print(i)
    sleep(10)

    for i in range(10):  # 122
        for j in range(10):
            print(i, j)

    ```

### TEST

```py
# question 1: 
def f(n):
    if n <= 1:
        return 1
    return f(n - 1) + f(n - 1)

# branches^depth  Time complexity:  O(2^N) space complexity:O(N)
```

- 40 min , tecnical: 70%code AND problem soving
-
- CTO
- CEO

```python
# O(log N) <  O(N) < O(N^2)
# O(N^2) isnt always better than O(N)

def func1(n): # O(N +100) = O(N)
    for i in range(n):
        ans = i*2
        print(f"{i} * 2 = {ans}")
    
    for i in range(100):
        print("OMG I LOVE MADEEHA SO MUCH")
    
def func2(n): # O(N/3) = O(N)
    for i in range(n):
        ans = i*3
        print(f"{i} * 3 = {ans}")
        
def func3(n): # O(N *N/2) = O(N^2/2) = O(N^2)
    for i in range(n):
        for j in range(i // 2):
            ans = i*j
            print(f"{i} * {j} = {i*j}")

    sleep(1000)
    
def func4(n): # O(log N)
    # assume tree represents a binary search tree
    
    low = 0
    high = len(tree) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        # If x is greater, ignore left half
        if tree[mid] < x:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif tree[mid] > x:
            high = mid - 1
 
        # means x is present at mid
        else:
            return mid
 
    # If we reach here, then the element was not present
    return -1

```

### Chapter

- 12

### Arrays and Strings

#### Hash Tables

- Array of linked lists and a hash code function.
- How to insert a value into a hash table?
  - 1. compute the hash code
  - 2. map the hash code to an index in the array
- worst case: O(N)
- average case: O(1)
- Alternative: use a balanced binary search tree
- ArrayList is a resizable arr
Example:

```bash
"hi" -> 10320 -> 0 -> "hi" , "abc"
               - 1
              -  2
"abc" -> 980 -   3
```
