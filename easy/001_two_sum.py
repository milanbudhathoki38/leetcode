# 1. Two Sum
# Difficulty: Easy
# Link: https://leetcode.com/problems/two-sum/
# Time Complexity: O(n²)
# Space Complexity: O(1)

class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]