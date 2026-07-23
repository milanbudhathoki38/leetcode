# 125. Valid Palindrome
# Difficulty: Easy
# Topic: Strings, Two Pointers
# Link: https://leetcode.com/problems/valid-palindrome/

# ----------------------------
# Problem:
# A phrase is a palindrome if after converting all uppercase
# letters to lowercase and removing all non-alphanumeric
# characters, it reads the same forward and backward.
# ----------------------------

# Approach: Clean then Two Pointers
# - clean string: keep only alphanumeric chars, lowercase all
# - left pointer from start, right pointer from end
# - compare characters moving inward — mismatch = not palindrome
# - if pointers cross without mismatch = palindrome
# Time: O(n) | Space: O(n)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(char.lower() for char in s if char.isalnum())
        left = 0
        right = len(cleaned) - 1
        while left < right:
            if cleaned[left] != cleaned[right]:
                return False
            left += 1
            right -= 1
        return True


# ----------------------------
# Test cases
# ----------------------------
if __name__ == "__main__":
    sol = Solution()

    s = "A man, a plan, a canal: Panama"
    print(f"isPalindrome = {sol.isPalindrome(s)}")  # True

    s = "race a car"
    print(f"isPalindrome = {sol.isPalindrome(s)}")  # False

    s = " "
    print(f"isPalindrome = {sol.isPalindrome(s)}")  # True