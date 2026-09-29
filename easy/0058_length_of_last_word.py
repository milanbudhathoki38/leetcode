# 58. Length of Last Word
# Difficulty: Easy
# Topic: String
# Link: https://leetcode.com/problems/length-of-last-word/

# ----------------------------
# Problem:
# Given a string s consisting of words and spaces, return the length
# of the last word in the string. A word is a maximal substring
# consisting of non-space characters only.
# ----------------------------

# Approach: Split and index
# - Splitting on whitespace automatically drops extra spaces and
#   empty strings, so the last element is always the last real word.
# Time: O(n) — one pass to split the string | Space: O(n) — split creates a list of words

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        return len(words[-1])

# ----------------------------
# Test cases
# ----------------------------
if __name__ == "__main__":
    sol = Solution()
    print(f"{sol.lengthOfLastWord('Hello World')}")  # Expected: 5
    print(f"{sol.lengthOfLastWord('   fly me   to   the moon  ')}")  # Expected: 4