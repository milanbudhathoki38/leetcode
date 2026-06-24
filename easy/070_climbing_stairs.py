# 70. Climbing Stairs
# Difficulty: Easy
# Topic: Dynamic Programming, Math
# Link: https://leetcode.com/problems/climbing-stairs/

# ----------------------------
# Problem:
# You are climbing a staircase with n steps. Each time you can
# climb 1 or 2 steps. Return how many distinct ways you can
# climb to the top.
# ----------------------------

# Approach: Iterative Fibonacci (Bottom-up DP)
# - every stair n can be reached from n-1 (1 step) or n-2 (2 steps)
# - so ways(n) = ways(n-1) + ways(n-2) — pure Fibonacci
# - prev2 tracks ways for n-2, prev1 tracks ways for n-1
# - slide both forward each iteration, return prev1 at the end
# Time: O(n) | Space: O(1)

from typing import List

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        prev2 = 1
        prev1 = 2
        for i in range(3, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
        return prev1


# ----------------------------
# Test cases
# ----------------------------
if __name__ == "__main__":
    sol = Solution()

    print(f"n=2, ways={sol.climbStairs(2)}")  # ways=2
    print(f"n=3, ways={sol.climbStairs(3)}")  # ways=3
    print(f"n=5, ways={sol.climbStairs(5)}")  # ways=8