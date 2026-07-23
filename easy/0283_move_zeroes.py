# 283. Move Zeroes
# Difficulty: Easy
# Topic: Arrays, Two Pointers
# Link: https://leetcode.com/problems/move-zeroes/

# ----------------------------
# Problem:
# Given an integer array nums, move all 0s to the end while
# maintaining the relative order of non-zero elements.
# Must be done in-place without making a copy of the array.
# ----------------------------

# Approach: Two Pointers (write pointer)
# - k is the write pointer — next position for a non-zero value
# - i scans every element left to right
# - if nums[i] != 0: write it at nums[k], advance k
# - after loop: fill positions k to end with 0
# Time: O(n) | Space: O(1)

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        k = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[k] = nums[i]
                k += 1
        for j in range(k, len(nums)):
            nums[j] = 0


# ----------------------------
# Test cases
# ----------------------------
if __name__ == "__main__":
    sol = Solution()

    nums = [0, 1, 0, 3, 12]
    sol.moveZeroes(nums)
    print(f"result = {nums}")  # result = [1, 3, 12, 0, 0]

    nums = [0, 0, 1]
    sol.moveZeroes(nums)
    print(f"result = {nums}")  # result = [1, 0, 0]

    nums = [0]
    sol.moveZeroes(nums)
    print(f"result = {nums}")  # result = [0]