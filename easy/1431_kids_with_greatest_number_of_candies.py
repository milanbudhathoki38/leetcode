# 1431. Kids With the Greatest Number of Candies
# Difficulty: Easy
# Topic: Array, List Comprehension
# Link: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

# ----------------------------
# Problem:
# There are n kids with candies. You are given an integer array candies,
# where each candies[i] represents the number of candies the ith kid has,
# and an integer extraCandies, denoting the number of extra candies that
# you have. Return a boolean array result of length n, where result[i] is
# true if, after giving the ith kid all the extraCandies, they will have
# the greatest number of candies among all the kids, or false otherwise.
# Note that multiple kids can have the greatest number of candies.
# ----------------------------

# Approach: One-pass + list comprehension
# - Find the current max of candies in one pass (max())
# - For each kid, check if candy count + extraCandies >= max
# - Build the result list with a ternary comprehension
# Time: O(n)  —> single pass to find max, single pass to build result 
# Space: O(n) —> result list holds one entry per kid

from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        highest = max(candies)
        return [True if c + extraCandies >= highest else False for c in candies]

# ----------------------------
# Test cases
# ----------------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.kidsWithCandies([2, 3, 5, 1, 3], 3))   # expected: [True, True, True, False, True]
    print(sol.kidsWithCandies([4, 2, 1, 1, 2], 1))   # expected: [True, False, False, False, False]
    print(sol.kidsWithCandies([12, 1, 12], 10))      # expected: [True, False, True]