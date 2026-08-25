# 155. Min Stack
# Difficulty: Medium
# Topic: Stack
# Link: https://leetcode.com/problems/min-stack/

# ----------------------------
# Problem:
# Design a stack that supports push, pop, top, and retrieving the
# minimum element in constant time O(1).
# ----------------------------

# Approach: Two stacks in parallel
# - A regular stack holds every pushed value, normal LIFO behavior
# - A second "min stack" holds the minimum-so-far at each point in time
# - Every push adds to BOTH stacks, always — if the new value is the
#   new minimum, push it onto min_stack; otherwise push the current
#   top of min_stack again, so both stacks always stay the same length
# - Every pop removes from BOTH stacks together, which automatically
#   "forgets" a minimum that only existed because of the popped value
# Time: O(1) for all operations | Space: O(n)

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

# ----------------------------
# Test cases
# ----------------------------
if __name__ == "__main__":
    obj = MinStack()
    obj.push(5)
    obj.push(2)
    obj.push(7)
    print(obj.getMin())  # expected: 2
    obj.pop()
    print(obj.getMin())  # expected: 2
    obj.pop()
    print(obj.getMin())  # expected: 5
    print(obj.top())     # expected: 5