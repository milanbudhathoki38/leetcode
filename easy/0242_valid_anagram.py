# 242. Valid Anagram
# Difficulty: Easy
# Topic: Hashing, Sorting, String
# Link: https://leetcode.com/problems/valid-anagram/

# ----------------------------
# Problem:
# Given two strings s and t, return true if t is an anagram of s,
# and false otherwise. An anagram is a word formed by rearranging
# the letters of another, using all the original letters exactly once.
# ----------------------------

# Approach: Sorting
# - Two strings are anagrams if and only if they contain the same
#   characters with the same frequencies.
# - Sorting both strings and comparing them checks this directly.
# Time: O(n log n) — sorting dominates | Space: O(n) — sorted copies of both strings

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

# ----------------------------
# Test cases
# ----------------------------
if __name__ == "__main__":
    sol = Solution()
    print(f"{sol.isAnagram('anagram', 'nagaram')}")  # Expected: True
    print(f"{sol.isAnagram('rat', 'car')}")  # Expected: False