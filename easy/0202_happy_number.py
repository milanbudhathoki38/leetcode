# 202. Happy Number
# Difficulty: Easy
# Topic: Hash Set, Math
# Link: https://leetcode.com/problems/happy-number/

# ----------------------------
# Problem:
# A happy number is defined by repeatedly replacing n with the
# sum of squares of its digits until it reaches 1 (happy) or
# loops forever never reaching 1 (not happy). Return true if
# n is a happy number, false otherwise.
# ----------------------------

# Approach: Hash Set cycle detection
# - seen tracks every number visited so far
# - if n hits 1 → happy, return True
# - if n appears in seen → cycle detected, return False
# - inner loop extracts each digit via modulo, squares it, sums
# Time: O(log n) | Space: O(log n)

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            total = 0
            while n > 0:
                digit = n % 10
                total += digit ** 2
                n = n // 10
            n = total
        return True


# ----------------------------
# Test cases
# ----------------------------
if __name__ == "__main__":
    sol = Solution()

    print(f"n=19, happy={sol.isHappy(19)}")   # happy=True
    print(f"n=2, happy={sol.isHappy(2)}")     # happy=False
    print(f"n=1, happy={sol.isHappy(1)}")     # happy=True
    print(f"n=7, happy={sol.isHappy(7)}")     # happy=True