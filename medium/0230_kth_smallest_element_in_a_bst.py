# 230. Kth Smallest Element in a BST
# Difficulty: Medium
# Topic: Tree, Binary Search Tree, Recursion
# Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# ----------------------------
# Problem:
# Given the root of a binary search tree and an integer k, return the
# kth smallest value (1-indexed) among all node values in the tree.
# ----------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Approach: Inorder traversal
# - Inorder traversal (LEFT, NODE, RIGHT) on a BST visits values in
#   sorted order automatically
# - Collect the full sorted list, then the kth smallest is at index k-1
# Time: O(n) — visits every node once to build the sorted list 
# Space: O(n) — stores every node's value in the list, plus O(h) call stack

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values: list[int] = []
        self._inorder(root, values)
        return values[k - 1]

    def _inorder(self, node: Optional[TreeNode], values: list[int]) -> None:
        if node is None:
            return
        self._inorder(node.left, values)
        values.append(node.val)
        self._inorder(node.right, values)

# ----------------------------
# Test cases
# ----------------------------
if __name__ == "__main__":
    sol = Solution()

    root1 = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6))
    print(sol.kthSmallest(root1, 3))  # expected: 4