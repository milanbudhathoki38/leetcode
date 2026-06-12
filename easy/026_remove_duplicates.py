# 26. Remove Duplicates from Sorted Array
# Difficulty: Easy
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def removeDuplicates(self, nums):
        k = 1
        for j in range(1, len(nums)):
            if nums[j] != nums[j-1]:
                nums[k] = nums[j]
                k += 1
        return k

# Personal testing — not submitted to LeetCode
if __name__ == "__main__":
    sol = Solution()
    
    nums = [1, 1, 2]
    k = sol.removeDuplicates(nums)
    print(f"k = {k}, nums = {nums[:k]}")  # k = 2, nums = [1, 2]
    
    nums = [0,0,1,1,1,2,2,3,3,4,4,4,4]
    k = sol.removeDuplicates(nums)
    print(f"k = {k}, nums = {nums[:k]}")  # k = 5, nums = [0, 1, 2, 3, 4]