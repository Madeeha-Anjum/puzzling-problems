# Implementation of a stack using a python class
# Alternatively a stack can be list [] using append and pop functionality


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
