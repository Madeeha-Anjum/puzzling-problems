#  Do a benchmark test for how long it takes to calculate fibbanachhi sequence from 1 to 50 with and without memorization and explain why memorization makes it faster - how many less calculations does the computer have to do or like how much faster is it


import timeit


def fib1(n):
    """
    fib(0) = 0
    fib(1) = 1
    fib(n) = fib(n-1) + fib(n-2)  for n > 1
    """

    if n <= 1:
        return 1

    return fib1(n - 1) + fib1(n - 2)


# using memoization


def fib2(n, memo={}):

    if n <= 1:
        return 1

    if n in memo:
        return memo[n]

    memo[n] = fib2(n - 1, memo) + fib2(n - 2, memo)

    return memo[n]


import time

if __name__ == "__main__":
    start = time.time()
    for i in range(1, 100):
        fib2(i)
    end = time.time()
    print(end - start)
