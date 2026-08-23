# 258. Add Digits
# Difficulty: Easy
# Topic: Math
# Link: https://leetcode.com/problems/add-digits/

# ----------------------------
# Problem:
# Given an integer num, repeatedly add all its digits until
# the result has only one digit. Return that digit.
# ----------------------------

# Approach: Repeated digit summing
# - While num has more than one digit, peel off digits with % 10
#   and // 10, summing them into total
# - Replace num with that total and repeat until num < 10
# Time: O(1) in practice (numbers shrink fast) | Space: O(1)

class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            total = 0
            while num > 0:
                digit = num % 10
                total += digit
                num = num // 10
            num = total

        return num

# ----------------------------
# Test cases
# ----------------------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.addDigits(38))   # expected: 2
    print(sol.addDigits(0))    # expected: 0
    print(sol.addDigits(9))    # expected: 9
    print(sol.addDigits(132))  # expected: 6  (1+3+2=6)