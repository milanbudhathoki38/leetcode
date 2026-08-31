# 225. Implement Stack using Queues
# Difficulty: Easy
# Topic: Stack, Design, Queue
# Link: https://leetcode.com/problems/implement-stack-using-queues/

# ----------------------------
# Problem:
# Implement a last-in-first-out (LIFO) stack using only two queues. The
# implemented stack should support push, top, pop, and empty, using only
# standard queue operations (push to back, pop from front, peek front,
# size, is empty).
# ----------------------------

# Approach: One queue, rotate on push
# - push(x): add x to the back, then rotate every OTHER element from
#   front to back, one at a time, so x ends up at the front
# - Since the most recent push is always at the front, pop/top/empty
#   become trivial — just look at (or remove) the front
#  Time: push is O(n) — rotates up to n elements each call | pop, top, empty are O(1) — front is always ready 
#  Space: O(n) — stores all n elements in one queue

from collections import deque

class MyStack:
    def __init__(self):
        self.stack = deque()

    def push(self, x: int) -> None:
        self.stack.append(x)
        for _ in range(len(self.stack) - 1):
            front = self.stack.popleft()
            self.stack.append(front)

    def pop(self) -> int:
        return self.stack.popleft()

    def top(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return len(self.stack) == 0

# ----------------------------
# Test cases
# ----------------------------
# ----------------------------
# Test cases
# ----------------------------
if __name__ == "__main__":
    myStack = MyStack()
    myStack.push(1)
    myStack.push(2)
    myStack.push(3)
    print(myStack.top())     # expected: 3 (most recent push)
    print(myStack.pop())     # expected: 3
    print(myStack.top())     # expected: 2 (now the new "top")
    myStack.push(4)
    print(myStack.top())     # expected: 4
    print(myStack.pop())     # expected: 4
    print(myStack.pop())     # expected: 2
    print(myStack.empty())   # expected: False (1 is still in there)
    print(myStack.pop())     # expected: 1
    print(myStack.empty())   # expected: True (nothing left)