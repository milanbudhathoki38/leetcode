# 9. Palindrome Number
# Difficulty: Easy
# Topic: Math
# Link: https://leetcode.com/problems/palindrome-number/

# ----------------------------
# Problem:
# Given an integer x, return true if x is a palindrome, and false
# otherwise. A palindrome reads the same forwards and backwards.
# ----------------------------

# Approach: Convert to string and compare
# - Negative numbers can never be palindromes (the minus sign breaks it).
# - Otherwise, convert to a string and check if it reads the same reversed.
# Time: O(n) — n is the number of digits | Space: O(n) — string conversion

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        s = str(x)
        return s == s[::-1]

# ----------------------------
# Test cases
# ----------------------------
if __name__ == "__main__":
    sol = Solution()
    print(f"{sol.isPalindrome(121)}")  # Expected: True
    print(f"{sol.isPalindrome(-121)}")  # Expected: False