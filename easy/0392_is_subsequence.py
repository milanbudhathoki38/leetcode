# 392. Is Subsequence
# Difficulty: Easy
# Topic: Two Pointers, String
# Link: https://leetcode.com/problems/is-subsequence/

#--------------------------
# Problem:
# Given strings s and t, return True if s is a subsequence of t.
# Characters must appear in the same order, but they do not
# need to be next to each other.
#--------------------------

# Approach: Two Pointers
# - i tracks the next character needed from s.
# - j scans through t.
# - When characters match, move i forward.
# - Always move j forward.
# - If i reaches len(s), every character in s was matched.
# Time: O(len(t)) | Space: O(1)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1

            j += 1

        if i == len(s):
            return True

        return False

#--------------------------
# Test cases
#--------------------------

if __name__ == "__main__":
    sol = Solution()

    s, t = "abc", "ahbgdc"
    print(f"isSubsequence = {sol.isSubsequence(s, t)}")  # True

    s, t = "axc", "ahbgdc"
    print(f"isSubsequence = {sol.isSubsequence(s, t)}")  # False

    s, t = "", "abc"
    print(f"isSubsequence = {sol.isSubsequence(s, t)}")  # True

    s, t = "abc", ""
    print(f"isSubsequence = {sol.isSubsequence(s, t)}")  # False

    s, t = "abc", "acb"
    print(f"isSubsequence = {sol.isSubsequence(s, t)}")  # False

    s, t = "aaa", "aa"
    print(f"isSubsequence = {sol.isSubsequence(s, t)}")  # False