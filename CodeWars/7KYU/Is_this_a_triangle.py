def is_triangle(a, b, c):
    # code here
    """
    true if a triangle can be built with the sides of given length and false in any other case.
    """
    # Triangle: h -> Longest side or equal
    # If the sum of any two sides is greater than the third side

    return True if a + b > c and a + c > b and b + c > a else False


if __name__ == "__main__":
    assert is_triangle(1, 2, 2) == True
    assert is_triangle(7, 2, 2) == False
