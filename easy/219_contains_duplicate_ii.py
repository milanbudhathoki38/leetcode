# 219. Contains Duplicate II
# Difficulty: Easy
# Topic: Hash Map, Array
# Link: https://leetcode.com/problems/contains-duplicate-ii/

# ----------------------------
# Problem:
# Given an integer array nums and an integer k, return true if
# there are two distinct indices i and j such that nums[i] == nums[j]
# and abs(i - j) <= k.
# ----------------------------

# Approach: Dict of Last Seen Index
# - store each number's most recent index in a dict as we scan
# - if we see a number again, check the distance to its last index
# - if distance <= k, return True immediately
# - always update the dict with the current index, whether it matched or not
# Time: O(n) | Space: O(n)

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen_indices = {}
        for i in range(len(nums)):
            current = nums[i]
            if current in seen_indices:
                last_index = seen_indices[current]
                if abs(i - last_index) <= k:
                    return True
            seen_indices[current] = i
        return False


# ----------------------------
# Test cases
# ----------------------------
if __name__ == "__main__":
    sol = Solution()

    nums, k = [1, 2, 3, 1], 3
    print(f"containsNearbyDuplicate = {sol.containsNearbyDuplicate(nums, k)}")  # True

    nums, k = [1, 0, 1, 1], 1
    print(f"containsNearbyDuplicate = {sol.containsNearbyDuplicate(nums, k)}")  # True

    nums, k = [1, 2, 3, 1, 2, 3], 2
    print(f"containsNearbyDuplicate = {sol.containsNearbyDuplicate(nums, k)}")  # False