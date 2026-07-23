# 509. Fibonacci Number
# Difficulty: Easy
# Topic: Math, Dynamic Programming, Recursion
# Link: https://leetcode.com/problems/fibonacci-number/

# ----------------------------
# Problem:
# The Fibonacci sequence is defined as F(0) = 0, F(1) = 1, and
# F(n) = F(n-1) + F(n-2) for n > 1. Given n, return F(n).
# ----------------------------

# Approach: Iterative Sliding Window
# - track the two previous Fibonacci values (prev2, prev1)
# - slide the window forward each step: prev2 <- prev1, prev1 <- current
# - avoids recursion overhead and redundant recomputation
# Time: O(n) | Space: O(1)


class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        prev2 = 0
        prev1 = 1
        for i in range(2, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
        return prev1


# ----------------------------
# Test cases
# ----------------------------
if __name__ == "__main__":
    sol = Solution()

    n = 4
    print(f"fib = {sol.fib(n)}")  # 3

    n = 2
    print(f"fib = {sol.fib(n)}")  # 1

    n = 0
    print(f"fib = {sol.fib(n)}")  # 0