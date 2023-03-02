# Elementary problems
# https://adriann.github.io/programming_problems.html


from functools import reduce


def main():
    pass


def mysum(n):
    lst = list(range(1, n))
    return reduce((lambda x, y: x + y), lst)


def product(n):
    lst = list(range(1, n))
    return reduce((lambda x, y: x * y), lst)


if __name__ == "__main__":

    # ------------------------- Q 8 ----------------------------
    # print all prime numbers: a whole number greater than 1 that cannot be exactly divided by any whole number other than itself and 1 (e.g. 2, 3, 5, 7, 11).
    lst = list(range(1, 100))
    prime = []
    # a % b == 0 -> means its perfectyl divisable aka no remander

    for item in lst:
        # print(item, prime)
        # check if it haas a factor between 1 and itself
        is_prime = True
        for i in range(2, item):
            if (item % i) == 0:
                is_prime = False
        if is_prime:
            prime.append(item)

    print(prime)

    # ------------------------- Q 10 ----------------------------
    # Write a program that prints the next 20 leap years.
    # leap year -> a year that contains 366 days with February 29 as the extra day, ~ every 4 years
    # Leap year -> numbers that are divisible by 4 except years that are divisible by 100
    # 2023 - 2043 20 years
    lst = list(range(23, 43))
    leap_years = []

    for i in lst:
        # except 400
        if i % 100 == 0:
            continue
        if i % 4 == 0:
            leap_years.append(f"20{i}")

    print(leap_years)

    # ------------------------- Q 11 ----------------------------
    # sum of an alternating series
    k = list(range(1, 10**6))

    formula = lambda k: 4 * (((-1) ** (k + 1)) / (2 * k - 1))
    sum = 0
    for i in k:
        sum = sum + formula(i)

    print(sum)

    # ------------------------- Q 2,3 ----------------------------

    name = input()
    if name == "Alice" or name == "Bob":
        print("Welcome", name)

    else:
        print("Welcome")
    # ------------------------- Q 4 ----------------------------

    n = int(input())
    # sum of numbers 1 to n
    # create list
    lst = list(range(1, n))
    # lambda function for sum
    sum = reduce((lambda x, y: x + y), lst)
    print("sum", sum)
    # ------------------------- Q 5 ----------------------------
    # modify it: only multiples of 3 are considered
    n = int(input())
    lst = list(range(1, n))
    # create a list multiples of 3
    lst = list(filter(lambda x: x % 3 == 0, lst))
    # lambda function for sum of lst
    sum = reduce((lambda x, y: x + y), lst)

    print("sum", sum)
    # ------------------------- Q 6 ----------------------------
    n = int(input())
    # choose 1->sum 2->product
    option = int(input("choose 1 or 2: "))
    if option == 1:
        ans = mysum(n)
    if option == 2:
        ans = product(n)

    print("Sum or product", ans)

    # ------------------------- Q 7 ----------------------------
    #  multiplication table for numbers up to 12
    rows, cols = (13, 13)
    # matrix = [[0] * cols] * rows # wrong becase this create pointers
    # for row in matrix:
    #     print(row)
    # Create a 2D array of size rows x cols
    matrix = [[0 for i in range(cols)] for j in range(rows)]

    # Another way to create a 2D array of size rows x cols
    matrix = []
    for row in range(rows):
        matrix.append([])
        for col in range(cols):
            matrix[row].append(0)

    # iterate through the 2D array, and set each element to the product of its row and column
    for row in range(rows):
        for col in range(cols):
            matrix[row][col] = (row + 1) * (col + 1)

    print(matrix)
