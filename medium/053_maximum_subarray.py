# 53. Maximum Subarray
# Difficulty: Medium
# Topic: Arrays, Dynamic Programming
# Link: https://leetcode.com/problems/maximum-subarray/

# ----------------------------
# Problem:
# Given an integer array nums, find the subarray with the
# largest sum, and return its sum.
# ----------------------------

# Approach: Kadane's Algorithm
# - current_sum = best sum of a subarray ending exactly at index i
# - at each step: extend previous subarray, or start fresh here?
#   current_sum = max(nums[i], current_sum + nums[i])
# - best_sum tracks the best sum seen anywhere so far
# Time: O(n) | Space: O(1)

class Solution:
    def maxSubArray(self, nums):
        current_sum = nums[0]
        best_sum = nums[0]

        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            best_sum = max(best_sum, current_sum)

        return best_sum


# ----------------------------
# Test cases
# ----------------------------
if __name__ == "__main__":
    sol = Solution()

    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"max_sum = {sol.maxSubArray(nums)}")  # max_sum = 6

    nums = [1]
    print(f"max_sum = {sol.maxSubArray(nums)}")  # max_sum = 1

    nums = [5, 4, -1, 7, 8]
    print(f"max_sum = {sol.maxSubArray(nums)}")  # max_sum = 23