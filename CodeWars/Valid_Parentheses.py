#  list as a stack instead of a class Stack


def valid_parentheses(string):
    # stack if first in last out
    #  pop from the stack and match with the first
    stack = []
    for val in string:

        if val == "(":
            stack.append(val)

        if val == ")":
            # pop from the stack and see if its a matching bracket
            if not stack or stack.pop() != "(":
                return False

    if stack:
        return False

    return True


if __name__ == "__main__":
    assert valid_parentheses("(())((()())())") == True
    assert valid_parentheses("  (") == False
    assert valid_parentheses("") == True
    assert valid_parentheses("hi(hi)()") == True
    assert valid_parentheses("hi())(") == False
