# 268. Missing Number
# Difficulty: Easy
# Topic: Math, Array
# Link: https://leetcode.com/problems/missing-number/

# ----------------------------
# Problem:
# Given an array nums containing n distinct numbers in the
# range [0, n], return the one number that is missing.
# ----------------------------

# Approach: Gauss Sum Formula
# - sum of all integers 0 to n = n * (n+1) / 2
# - subtract the actual sum of nums from the expected sum
# - the difference is the missing number
# Time: O(n) | Space: O(1)

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum


# ----------------------------
# Test cases
# ----------------------------
if __name__ == "__main__":
    sol = Solution()

    nums = [3, 0, 1]
    print(f"missingNumber = {sol.missingNumber(nums)}")  # 2

    nums = [0, 1]
    print(f"missingNumber = {sol.missingNumber(nums)}")  # 2

    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    print(f"missingNumber = {sol.missingNumber(nums)}")  # 8