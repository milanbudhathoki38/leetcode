# 1051. Height Cheecker 
# Difficulty: Easy
# Topic: Array, Sorting
# Link: https://leetcode.com/problems/height-checker/

# ----------------------------
# Problem:
# Given heights, compare it to the array sorted in non-decreasing
# order. Return the number of indices where they differ.
# ----------------------------

# Approach: Sort and Compare
# - sort a copy of heights to get the "expected" order
# - walk both arrays in parallel, count mismatched positions
# Time: O(n log n) | Space: O(n)


from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                count += 1
        return count
    


if __name__ == "__main__":
    sol = Solution()
    print(sol.heightChecker([1, 1, 4, 2, 1, 3]))    # 3
    print(sol.heightChecker([5, 1, 2, 3, 4]))       # 5
    print(sol.heightChecker([1, 2, 3, 4, 5]))       # 0
