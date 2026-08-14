# 303. Range Sum Query - Immutable
# Difficulty: Easy
# Topic: Prefix Sum, Array, Design 
# Link: https://leetcode.com/problems/range-sum-query-immutable/

# ------------------------------
# Problem:
# Given an integer array nums, implement NumArray:
# - NumArray(nums): initializes the object with the array
# - sumRange(left, right): returns the sum of nums[left...right],
#   inclusive. This method can be called many times.
# ------------------------------

# Approach: Prefix Sum
# - build self.prefix ONCE, in the constructor. self.prefix[i] holds
#  the running total of everything BEFORE index i (like writing down
#  your bank balance after opening each envelope of crash, one at a 
#  time — self.prefix[0] = 0 is your balance before opening anything,
#   a fixed starting point, not something calculated).
# - self.prefix is one element longer than nums, so self.prefix[0]
#   can safely represent "sum of zero elements."
# - sumRange never touches nums again after the constructor — it only
#   ever reads two values out of the already-built self.prefix and
#   subtracts them. No looping needed per call.
# - sumRange(left, right) = prefix[right+1] - prefix[left]:
#   prefix[right+1] is "everything through right," prefix[left] is
#   "everything before left" — subtracting leaves exactly the range
#   asked for.
# Time: constructor O(n), sumRange O(1) per call | Space: O(n)

# Note on self.prefix[0]:
# self.prefix[0] is NOT something we calculate from a "previous"
# value we don't know yet. The line `self.prefix = [0] * (len(nums)+1)`
# runs BEFORE the loop even starts, and it sets EVERY slot to 0 right
# away — including self.prefix[0]. So by the time the loop reaches
# i=0, self.prefix[0] already exists and is already 0. The line
# `self.prefix[1] = self.prefix[0] + nums[0]` is just reading that
# already-set 0 and adding nums[0] to it — nothing mysterious, no
# "unknown previous value." self.prefix[0] = 0 is a fixed starting
# point by definition (your balance before opening any envelopes),
# not a value built from something earlier in the loop.

from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefix[i + 1] = self.prefix[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]

    #--------------------------
    # Test cases 
    # -------------------------

if __name__ == "__main__":
    obj = NumArray([-2, 0, 3, -5, 2, -1])
    print(f"sumRange(0, 2) = {obj.sumRange(0, 2)}") # 1
    print(f"sumRange(2, 5) = {obj.sumRange(2 ,5)}") # -1
    print(f"sumRange(0, 5) = {obj.sumRange(0, 5)}") # -3

    obj2 = NumArray([4, -3, 2, 8, -1, 5])
    print(f"sumRange(1, 4) = {obj2.sumRange(1, 4)}") # 6
