# 136. Single Number
# Difficulty: Easy
# Topic: Hash Set, Bit Manipulation
# Link: https://leetcode.com/problems/single-number/

# ----------------------------
# Problem:
# Given a non-empty array of integers nums, every element
# appears twice except for one. Find that single one.
# ----------------------------

# Approach: Set as a Pairing Tracker
# - use a set to track numbers seen an odd number of times
# - if a number is already in the set, it just got paired up -> remove it
# - if not, this is its first appearance -> add it
# - whatever remains in the set after the loop is the unpaired number
# Time: O(n) | Space: O(n)

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                seen.remove(nums[i])
            else:
                seen.add(nums[i])
        return seen.pop()


# ----------------------------
# Test cases
# ----------------------------
if __name__ == "__main__":
    sol = Solution()

    nums = [4, 1, 2, 1, 2]
    print(f"singleNumber = {sol.singleNumber(nums)}")  # 4

    nums = [2, 2, 1]
    print(f"singleNumber = {sol.singleNumber(nums)}")  # 1

    nums = [1]
    print(f"singleNumber = {sol.singleNumber(nums)}")  # 1