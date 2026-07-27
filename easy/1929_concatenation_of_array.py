# 1929. Concatenation of Array
# Difficulty: Easy
# Topic: Array
# Link: https://leetcode.com/problems/concatenation-of-array/

# ----------------------------
# Problem:
# Given an array nums, return an array ans of length 2n where
# ans[i] == nums[i] and ans[i+n] == nums[i].
# ----------------------------

# Approach: List Concatenation
# - Python's + operator on two lists joins them end to end
# Time: O(n) | Space: O(n)

from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums


if __name__ == "__main__":
    sol = Solution()
    print(sol.getConcatenation([1, 2, 1]))  # [1, 2, 1, 1, 2, 1]