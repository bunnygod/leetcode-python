# class MinStack:

#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.stack = []
#         self.min_stack = []


#     def push(self, val: int) -> None:
#         self.stack.append(val)

#         if not self.min_stack or val <= self.min_stack[-1]:
#             self.min_stack.append(val)


#     def pop(self) -> None:
#         if self.min_stack and self.stack[-1] == self.min_stack[-1]:
#             self.min_stack.pop()

#         self.stack.pop()

#     def top(self) -> int:
#         return self.stack[-1]

#     def getMin(self) -> int:
#         return self.min_stack[-1]

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_stack = []

    def push(self, val: int) -> None:
        if not self.min_stack or val <= self.min_stack[-1][1]:
            self.min_stack.append((val, val))
        else:
            self.min_stack.append((val, self.min_stack[-1][1]))

    def pop(self) -> None:
        self.min_stack.pop()

    def top(self) -> int:
        return self.min_stack[-1][0]

    def getMin(self) -> int:
        return self.min_stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()