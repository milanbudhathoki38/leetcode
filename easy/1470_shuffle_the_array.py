# 1470. Shuffle the Array
# Difficulty: Easy
# Topic: Array
# Link: https://leetcode.com/problems/shuffle-the-array/

# ----------------------------
# Problem:
# Given nums of length 2n, where the first n elements are x1..xn
# and the last n are y1..yn, return the array in the form
# x1,y1,x2,y2,...,xn,yn.
# ----------------------------

# Approach: Interleave with an Index Loop
# - loop i from 0 to n-1
# - at each step, take nums[i] (the x side) and nums[i+n] (the y side)
# - append both into result, in x,y order
# Time: O(n) | Space: O(n)

from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[i + n])
        return result


# ----------------------------
# Test cases
# ----------------------------
if __name__ == "__main__":
    sol = Solution()

    nums, n = [2, 5, 1, 3, 4, 7], 3
    print(f"shuffle = {sol.shuffle(nums, n)}")  # [2, 3, 5, 4, 1, 7]

    nums, n = [1, 2, 3, 4, 4, 3, 2, 1], 4
    print(f"shuffle = {sol.shuffle(nums, n)}")  # [1, 4, 2, 3, 3, 2, 4, 1]

    nums, n = [1, 1, 2, 2], 2
    print(f"shuffle = {sol.shuffle(nums, n)}")  # [1, 2, 1, 2]

    nums, n = [10, 20, 30, 40, 50, 60], 3
    print(f"shuffle = {sol.shuffle(nums, n)}")  # [10, 40, 20, 50, 30, 60]