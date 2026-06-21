# 20. Valid Parentheses
# Difficulty: Easy
# Topic: Stack
# Link: https://leetcode.com/problems/valid-parentheses/

# ----------------------------
# Problem:
# Given a string s containing just the characters '(', ')', '{', '}',
# '[' and ']', determine if the input string is valid. Open brackets
# must be closed by the same type, in the correct order, and every
# close bracket must have a corresponding open bracket.
# ----------------------------

# Approach: Stack
# - pairs maps each closing bracket to its matching opening bracket
# - for each char: if it's an opening bracket, push it onto the stack
# - if it's a closing bracket, check the top of the stack:
#   - if stack is empty OR top doesn't match -> invalid, return False
#   - otherwise pop the stack (that pair is resolved)
# - at the end, stack must be empty for the string to be valid
# Time: O(n) | Space: O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in pairs:
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)

        return not stack


# ----------------------------
# Test cases
# ----------------------------
if __name__ == "__main__":
    sol = Solution()

    s = "()"
    print(f"s = {s!r}, valid = {sol.isValid(s)}")  # valid = True

    s = "()[]{}"
    print(f"s = {s!r}, valid = {sol.isValid(s)}")  # valid = True

    s = "(]"
    print(f"s = {s!r}, valid = {sol.isValid(s)}")  # valid = False

    s = "([)]"
    print(f"s = {s!r}, valid = {sol.isValid(s)}")  # valid = False

    s = "{[]}"
    print(f"s = {s!r}, valid = {sol.isValid(s)}")  # valid = True