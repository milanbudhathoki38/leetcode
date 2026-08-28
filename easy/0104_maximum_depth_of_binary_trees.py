# 104. Maximum Depth of Binary Tree
# Difficulty: Easy
# Topic: Tree, Depth-First Search, Binary Tree, Recursion
# Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/

# ----------------------------
# Problem:
# Given the root of a binary tree, return its maximum depth — the number
# of nodes along the longest path from the root node down to the
# farthest leaf node.
# ----------------------------

# Approach: Recursion (DFS)
# - Base case: an empty tree (root is None) has depth 0
# - Recursively find the depth of the left and right subtrees
# - Combine: 1 (for the current root) + whichever subtree is deeper
# Time: O(n) — visits every node in the tree exactly once | Space: O(h) — call stack depth equals tree height, worst case O(n) for a skewed tree

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return max(left_depth, right_depth) + 1

# ----------------------------
# Test cases
# ----------------------------
if __name__ == "__main__":
    sol = Solution()

    # Tree: [3,9,20,null,null,15,7] -> depth 3
    root1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(sol.maxDepth(root1))  # expected: 3

    # Tree: [1,null,2] -> depth 2
    root2 = TreeNode(1, None, TreeNode(2))
    print(sol.maxDepth(root2))  # expected: 2

    # Empty tree
    print(sol.maxDepth(None))   # expected: 0