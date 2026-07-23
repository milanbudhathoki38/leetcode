# 198. House Robber
# Difficulty: Medium
# Topic: Arrays, Dynamic Programming
# Link: https://leetcode.com/problems/house-robber/

# ----------------------------
# Problem:
# Given an array nums representing money in each house, return
# the maximum amount you can rob without robbing two adjacent houses.
# ----------------------------

# Approach: Bottom-up DP (Climbing Stairs family)
# - at each house, choose: skip it (keep prev1) or rob it (nums[i] + prev2)
# - current = max(prev1, nums[i] + prev2)
# - prev2 tracks best up to two houses back
# - prev1 tracks best up to previous house
# - slide both forward each iteration
# Time: O(n) | Space: O(1)

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        prev2 = nums[0]
        prev1 = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            current = max(prev1, nums[i] + prev2)
            prev2 = prev1
            prev1 = current
        return prev1


# ----------------------------
# Test cases
# ----------------------------
if __name__ == "__main__":
    sol = Solution()

    nums = [1, 2, 3, 1]
    print(f"max_rob = {sol.rob(nums)}")  # max_rob = 4

    nums = [2, 7, 9, 3, 1]
    print(f"max_rob = {sol.rob(nums)}")  # max_rob = 12

    nums = [2, 1]
    print(f"max_rob = {sol.rob(nums)}")  # max_rob = 2