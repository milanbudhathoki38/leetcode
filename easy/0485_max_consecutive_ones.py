# 485. Max Consecutive Ones
# Difficulty: Easy
# Topic: Array
# Link: https://leetcode.com/problems/max-consecutive-ones/

# ----------------------------
# Problem:
# Given a binary array nums, return the maximum number of
# consecutive 1s in the array.
# ----------------------------

# Approach: Single pass with a running count
# - Keep a count of the current streak of 1s and the best streak seen so far.
# - A 1 extends the streak, and a 0 resets it to zero.
# Time: O(n) — one pass through the list | Space: O(1) — two variables only

class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        count = 0
        max_count = 0

        for num in nums:
            if num == 1:
                count += 1
                max_count = max(count, max_count)
            else:
                count = 0

        return max_count

# ----------------------------
# Test cases
# ----------------------------
if __name__ == "__main__":
    sol = Solution()
    print(f"{sol.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1])}")  # Expected: 3
    print(f"{sol.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1])}")  # Expected: 2