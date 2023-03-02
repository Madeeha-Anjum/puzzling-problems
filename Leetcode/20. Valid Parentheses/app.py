"""
Stacks: Abstract data type | push | pop
    -> push into the stack 
    -> pop the top one off
    -> LIFO: Last in first out
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = Stack()

        matching_bracket = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in ["(", "{", "["]:
                stack.push(char)
            else:
                if stack.empty():
                    return False

                if stack.pop() != matching_bracket[char]:
                    return False

        return stack.empty()


class Stack:
    def __init__(self):
        self.elements = []

    def push(self, data):
        self.elements.append(data)
        # print(f"PUSH: {self.elements}")

    def pop(self):
        element = self.elements.pop()
        # print(f"POP: {self.elements}")
        return element

    def size(self):
        return len(self.elements)

    def empty(self):
        return True if self.size() == 0 else False

    def peek(self):
        """
        See whats at the top of the stack
        """
        return self.elements[-1]

    def print(self):
        print(self.elements)


if __name__ == "__main__":
    assert Solution().isValid("()") == True
    assert Solution().isValid("(){)") == False
    assert Solution().isValid("(())") == True
    assert Solution().isValid("(()())") == True

    assert Solution().isValid("(()") == False
    assert Solution().isValid("{()") == False
    assert Solution().isValid("{()}") == True
    assert Solution().isValid("") == True
    assert Solution().isValid("())") == False
