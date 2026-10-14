# 35. Search Insert Position
# Difficulty: Easy
# Topic: Array, Binary Search
# Link: https://leetcode.com/problems/search-insert-position/

# ----------------------------
# Problem:
# Given a sorted array of distinct integers and a target value, return
# the index if the target is found. If not, return the index where it
# would be if it were inserted in order. You must write an algorithm
# with O(log n) runtime complexity.
# ----------------------------

# Approach: Binary Search
# - Keep two pointers, left at the start and right at the end
# - Check the middle element on each loop
# - If it matches the target, return mid
# - If the middle is smaller than the target, move left to mid + 1
# - If the middle is bigger, move right to mid - 1
# - If the target is never found, left ends up exactly at the spot
#   where the target should be inserted, so return left
# Time: O(log n) — the search range is cut in half every loop | Space: O(1) — only a few pointers

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left


# ----------------------------
# Test cases
# ----------------------------
if __name__ == "__main__":
    sol = Solution()
    print(f"Test 1: {sol.searchInsert([1, 3, 5, 6], 5)}")  # Expected: 2
    print(f"Test 2: {sol.searchInsert([1, 3, 5, 6], 2)}")  # Expected: 1
    print(f"Test 3: {sol.searchInsert([1, 3, 5, 6], 7)}")  # Expected: 4
    print(f"Test 4: {sol.searchInsert([1, 3, 5, 6], 0)}")  # Expected: 0
    print(f"Test 5: {sol.searchInsert([1], 1)}")  # Expected: 0
