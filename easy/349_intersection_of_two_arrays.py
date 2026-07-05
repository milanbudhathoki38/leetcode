# 349. Intersection of Two Arrays
# Difficulty: Easy
# Topic: Arrays, Hash Set
# Link: https://leetcode.com/problems/intersection-of-two-arrays/

# ----------------------------
# Problem:
# Given two arrays nums1 and nums2, return an array of their
# intersection. Each element in the result must be unique.
# ----------------------------

# Approach: Hash Set intersection
# - convert both arrays to sets (removes duplicates automatically)
# - use & operator to find common elements between both sets
# - convert result back to list
# Time: O(n + m) | Space: O(n + m)

from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1 & set2)


# ----------------------------
# Test cases
# ----------------------------
if __name__ == "__main__":
    sol = Solution()

    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(f"result = {sol.intersection(nums1, nums2)}")  # result = [2]

    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    print(f"result = {sol.intersection(nums1, nums2)}")  # result = [9, 4]