# 1480. Running Sum of 1d Array
# Difficulty: Easy
# Topic: Array, Prefix Sum
# Link: https://leetcode.com/problems/running-sum-of-1d-array/

# ----------------------------
# Problem:
# Given an array nums, return the running sum where
# runningSum[i] = sum(nums[0]...nums[i]).
# ----------------------------

# Approach: Running Total Accumulator
# - keep a running total as we scan through nums
# - append the running total to result after each addition
# - result grows to the same length as nums
# Time: O(n) | Space: O(n)

from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        currentSum = 0
        result = []
        for num in nums:
            currentSum += num
            result.append(currentSum)
        return result


# ----------------------------
# Test cases
# ----------------------------
if __name__ == "__main__":
    sol = Solution()

    nums = [1, 2, 3, 4]
    print(f"runningSum = {sol.runningSum(nums)}")  # [1, 3, 6, 10]

    nums = [1, 1, 1, 1, 1]
    print(f"runningSum = {sol.runningSum(nums)}")  # [1, 2, 3, 4, 5]

    nums = [3, 1, 2, 10, 1]
    print(f"runningSum = {sol.runningSum(nums)}")  # [3, 4, 6, 16, 17]