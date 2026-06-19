# 27. Remove Element
# Difficulty: Easy
# Topic: Arrays, Two Pointers
# Link: https://leetcode.com/problems/remove-element/

# ----------------------------
# Problem:
# Given an array nums and a value val, remove all occurrences
# of val in-place. Return k — the count of elements != val.
# ----------------------------

# Approach: Two Pointers
# - k is the write pointer (where to place the next keeper)
# - i scans every element left to right
# - if nums[i] != val, write it at nums[k] and advance k
# Time: O(n) | Space: O(1)

class Solution:
    def removeElement(self, nums, val):
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k


# ----------------------------
# Test cases
# ----------------------------
if __name__ == "__main__":
    sol = Solution()

    nums = [3, 2, 2, 3]
    k = sol.removeElement(nums, 3)
    print(f"k={k}, nums={nums[:k]}")  # k=2, nums=[2, 2]

    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    k = sol.removeElement(nums, 2)
    print(f"k={k}, nums={nums[:k]}")  # k=5, nums=[0, 1, 3, 0, 4]