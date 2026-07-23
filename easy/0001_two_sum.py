# 1. Two Sum
# Difficulty: Easy
# Topic: Arrays, Brute Force
# Link: https://leetcode.com/problems/two-sum/

# ----------------------------
# Problem:
# Given an array of integers nums and an integer target, return the
# indices of the two numbers such that they add up to target.
# Assume exactly one solution exists, and you may not use the same
# element twice.
# ----------------------------

# Approach: Brute Force
# - check every possible pair of indices (i, j) where j > i
# - if nums[i] + nums[j] equals target, return their indices
# Time: O(n²) | Space: O(1)

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


# ----------------------------
# Test cases
# ----------------------------
if __name__ == "__main__":
    sol = Solution()

    nums = [2, 7, 11, 15]
    target = 9
    print(f"result = {sol.twoSum(nums, target)}")  # result = [0, 1]

    nums = [3, 2, 4]
    target = 6
    print(f"result = {sol.twoSum(nums, target)}")  # result = [1, 2]