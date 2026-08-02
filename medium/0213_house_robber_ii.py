# 213. House Robber II 
# Difficulty: Medium
# Topic: Dynamic Programming, Array
# Link: https://leetcode.com/problems/house-robber-ii/

#--------------------------
# Problem:
# Houses are arranged in a circle, so the first and last house are 
# adjacent. Given nums, return the maximum amount that can be robbed
# wihtout robbbing two adjacent houses.
#--------------------------

# Approach: Two Linear House RObber Passes
# - since it's circular, robbing boht the first and last is never alloed
# so the answer is the max of two seperate linear Hose RObber runs:
#   1) houses[0: n-1] (exclude the last house)
#   2) hoses[1: n] (exclude the last house)
# - each pass resues the standard sliding-window House Robber DP
# Time: O(n)  | Space: O(1)

from typing import List

class Solution:
    def rob(self, nums: List[int]) ->  int:
        if len(nums) == 1:
            return nums[0]

        def robLine(houses):
            prev2 = 0
            prev1 = 0 
            for money in houses:
                prev2, prev1 = prev1, max(prev1, prev2 + money)
            return prev1

        option1 = robLine(nums[:-1])
        option2 = robLine(nums[1:])
        return max(option1, option2)

#-----------------------------
# Test cases 
#-----------------------------

if __name__ == "__main__":
    sol = Solution()

nums = [2,3,2]
print(f"rob = {sol.rob(nums)}")  # 3

nums = [1,2,3,1]
print(f"rob = {sol.rob(nums)}") # 4

nums =[1,2,3]
print(f"rob = {sol.rob(nums)}") # 3

nums = [200]
print(f"rob = {sol.rob(nums)}") # 200 (single house, no circle issie)


nums = [1,2]
print(f"rob = {sol.rob(nums)}") # 2 (two houses are adjacent circularly, rob the bigger one)

nums = [1, 3, 1, 3, 100]
print(f"rob = {sol.rob(nums)}") # 103

nums = [5, 5, 10, 100, 10, 5] 
print(f"rob = {sol.rob(nums)}") # 110


