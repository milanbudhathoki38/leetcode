# 26. Remove Duplicates from Sorted Array
# Difficulty: Easy
# Topic: Arrays, Two Pointers
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# ----------------------------
# Problem:
# Given an integer array nums sorted in non-decreasing order, remove
# duplicates in-place such that each unique element appears only once.
# Return k — the number of unique elements.
# ----------------------------

# Approach: Two Pointers
# - k is the write pointer (where to place the next unique element)
# - j scans every element starting at index 1
# - since the array is sorted, duplicates are always neighbors
# - if nums[j] != nums[j-1], it's a new unique value: write it at nums[k], advance k
# Time: O(n) | Space: O(1)

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for j in range(1, len(nums)):
            if nums[j] != nums[j-1]:
                nums[k] = nums[j]
                k += 1
        return k


# ----------------------------
# Test cases
# ----------------------------
if __name__ == "__main__":
    sol = Solution()

    nums = [1, 1, 2]
    k = sol.removeDuplicates(nums)
    print(f"k = {k}, nums = {nums[:k]}")  # k = 2, nums = [1, 2]

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 4, 4, 4]
    k = sol.removeDuplicates(nums)
    print(f"k = {k}, nums = {nums[:k]}")  # k = 5, nums = [0, 1, 2, 3, 4]