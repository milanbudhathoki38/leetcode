# 383. Ransom Note
# Difficulty: Easy
# Topic: Hash Table, String, Counting
# Link: https://leetcode.com/problems/ransom-note/

# ----------------------------
# Problem:
# Given two strings ransomNote and magazine, return true if ransomNote
# can be constructed by using the letters from magazine, and false
# otherwise. Each letter in magazine can only be used once in
# ransomNote.
# ----------------------------

# Approach: Hash Map Letter Count
# - Count how many times each letter appears in magazine using a dictionary
# - Go through ransomNote one letter at a time
# - If the dictionary has none of that letter left, return False
# - Otherwise use one up by subtracting 1 from its count
# - If every letter in ransomNote was found, return True
# Time: O(m + n) — one pass over magazine and one over ransomNote | Space: O(1) — at most 26 lowercase letters in the dictionary

from typing import List


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counts = {}

        for letter in magazine:
            counts[letter] = counts.get(letter, 0) + 1

        for letter in ransomNote:
            if counts.get(letter, 0) == 0:
                return False
            counts[letter] -= 1

        return True


# ----------------------------
# Test cases
# ----------------------------
if __name__ == "__main__":
    sol = Solution()
    print(f"Test 1: {sol.canConstruct('a', 'b')}")  # Expected: False
    print(f"Test 2: {sol.canConstruct('aa', 'ab')}")  # Expected: False
    print(f"Test 3: {sol.canConstruct('aa', 'aab')}")  # Expected: True
    print(f"Test 4: {sol.canConstruct('ab', 'aab')}")  # Expected: True
