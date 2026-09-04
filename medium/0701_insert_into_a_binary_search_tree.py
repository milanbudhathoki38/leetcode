# 701. Insert into a Binary Search Tree
# Difficulty: Medium
# Topic: Tree, Binary Search Tree, Binary Tree
# Link: https://leetcode.com/problems/insert-into-a-binary-search-tree/

# ----------------------------
# Problem:
# Given the root of a binary search tree and a value to insert, insert
# the value into the BST, preserving BST ordering, and return the root
# of the tree after insertion. There may be multiple valid trees; any
# one that satisfies BST rules is accepted.
# ----------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Approach: Iterative walk using BST ordering
# - If the tree is empty, the new value becomes the root
# - Otherwise walk down comparing val against the current node
# - Smaller: go left, bigger: go right, until an empty spot is found
# - Place the new node there, always return the original root
# Time: O(h) — h is tree height, worst case O(n) for a skewed tree, O(log n) for a balanced tree 
#  Space: O(1) — iterative, no recursion used

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)

        current = root
        while current is not None:
            if val < current.val:
                if current.left is None:
                    current.left = TreeNode(val)
                    return root
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = TreeNode(val)
                    return root
                else:
                    current = current.right

        return root

# ----------------------------
# Test cases
# ----------------------------
if __name__ == "__main__":
    sol = Solution()

    root1 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
    result1 = sol.insertIntoBST(root1, 5)
    print(result1.right.left.val)  # expected: 5

    result2 = sol.insertIntoBST(None, 10)
    print(result2.val)  # expected: 10