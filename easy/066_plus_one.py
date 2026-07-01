# 66. Plus One
# Difficulty: Easy
# Topic: Arrays, Math
# Link: https://leetcode.com/problems/plus-one/

# ----------------------------
# Problem:
# Given an array of digits representing a non-negative integer
# (most significant digit first), add one to the number and
# return the resulting array of digits.
# ----------------------------

# Approach: Carry propagation (right to left)
# - walk backwards from the last digit
# - if current digit < 9: add 1, done immediately
# - if current digit == 9: set it to 0, carry continues left
# - if the carry survives past the first digit, every digit
#   was 9 — prepend a new leading 1 (e.g. 999 -> 1000)
# Time: O(n) | Space: O(1) excluding output array
# Note: in the worst case (all 9s) a new array is technically
# created via [1] + digits, making that specific case O(n) space.

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits


# ----------------------------
# Test cases
# ----------------------------
if __name__ == "__main__":
    sol = Solution()

    digits = [1, 2, 3]
    print(f"result = {sol.plusOne(digits)}")  # result = [1, 2, 4]

    digits = [4, 3, 2, 1]
    print(f"result = {sol.plusOne(digits)}")  # result = [4, 3, 2, 2]

    digits = [9]
    print(f"result = {sol.plusOne(digits)}")  # result = [1, 0]

    digits = [9, 9, 9]
    print(f"result = {sol.plusOne(digits)}")  # result = [1, 0, 0, 0]