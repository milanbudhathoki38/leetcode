# 217. Contains Duplicate
# Difficulty: Easy
# Topic: Arrays, Hash Set
# Link: https://leetcode.com/problems/contains-duplicate/

# ----------------------------
# Problem:
# Given an integer array nums, return true if any value appears
# at least twice, and false if every element is distinct.
# ----------------------------

# Approach: Hash Set
# - seen tracks every number we have visited so far
# - for each num: if it already exists in seen, it's a duplicate
# - otherwise add it to seen and keep going
# - if loop finishes with no duplicate found, return False
# Time: O(n) | Space: O(n)

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


# ----------------------------
# Test cases
# ----------------------------
if __name__ == "__main__":
    sol = Solution()

    nums = [1, 2, 3, 1]
    print(f"contains_duplicate = {sol.containsDuplicate(nums)}")  # True

    nums = [1, 2, 3, 4]
    print(f"contains_duplicate = {sol.containsDuplicate(nums)}")  # False

    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(f"contains_duplicate = {sol.containsDuplicate(nums)}")  # True