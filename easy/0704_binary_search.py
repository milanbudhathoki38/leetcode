# 704. Binary Search
# Difficulty: Easy
# Topic: Binary Search, Array
# Link: https://leetcode.com/problems/binary-search/

# ----------------------------
# Problem:
# Given a sorted array nums and a target, return target's index,
# or -1 if not found. Must run in O(log n) time.
# ----------------------------

# Approach: Classic Binary Search
# - maintain left/right pointers bounding the search space
# - check the middle element each step
# - if too small, discard the left half (left = mid + 1)
# - if too big, discard the right half (right = mid - 1)
# - halves the search space every iteration -> O(log n)
# Time: O(log n) | Space: O(1)

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.search([-1, 0, 3, 5, 9, 12], 9))   # 4
    print(sol.search([-1, 0, 3, 5, 9, 12], 2))   # -1