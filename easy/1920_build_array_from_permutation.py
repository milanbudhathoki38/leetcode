# 1920. Build Array from Permutation
# Difficulty: Easy
# Topic: Array
# Link: https://leetcode.com/problems/build-array-from-permutation/

# ----------------------------
# Problem:
# Given a zero-indexed array nums, build a new array ans where
# ans[i] = nums[nums[i]].
# ----------------------------

# Approach: Double Indexing
# - for each index i, first look up nums[i] to get a value
# - use that value AS a new index back into nums
# - nums[nums[i]] performs both lookups in one expression
# Time: O(n) | Space: O(n)

from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            result.append(nums[nums[i]])
        return result


# ----------------------------
# Test cases
# ----------------------------
if __name__ == "__main__":
    sol = Solution()

    nums = [0, 2, 1, 5, 3, 4]
    print(f"buildArray = {sol.buildArray(nums)}")  # [0, 1, 2, 4, 5, 3]

    nums = [5, 0, 1, 2, 3, 4]
    print(f"buildArray = {sol.buildArray(nums)}")  # [4, 5, 0, 1, 2, 3]