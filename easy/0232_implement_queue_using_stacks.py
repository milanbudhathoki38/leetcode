# 232. Implement Queue using Stacks
# Difficulty: Easy
# Topic: Stack, Queue, Design
# Link: https://leetcode.com/problems/implement-queue-using-stacks/

# ----------------------------
# Problem:
# Implement a first-in-first-out (FIFO) queue using only two stacks. The
# implemented queue should support push, peek, pop, and empty, using
# only standard stack operations (push to top, pop from top, peek top,
# size, is empty).
# ----------------------------

# Approach: Two stacks, transfer on demand
# - push(x): just append to stack_in, no extra work needed
# - pop/peek: if stack_out is empty, dump all of stack_in into stack_out
#   (this reverses the order, putting the oldest item on top of stack_out)
# - Only re-transfer when stack_out is empty, so old items already in the
#   right order aren't disturbed
# Time: amortized O(1) per operation — each element moves between the two stacks at most once, even though a single pop/peek can be O(n) worst case | Space: O(n) — total elements split across both stacks

class MyQueue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()

    def peek(self) -> int:
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out[-1]

    def empty(self) -> bool:
        return not self.stack_in and not self.stack_out

# ----------------------------
# Test cases
# ----------------------------
if __name__ == "__main__":
    q = MyQueue()
    q.push(1)
    q.push(2)
    print(q.peek())    # expected: 1
    print(q.pop())     # expected: 1
    print(q.empty())   # expected: False