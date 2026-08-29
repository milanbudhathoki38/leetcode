# 226. Invert Binary Tree
# Difficulty: Easy
# Topic: Tree, Depth-First Search, Binary Tree, Recursion
# Link: https://leetcode.com/problems/invert-binary-tree/

# ----------------------------
# Problem:
# Given the root of a binary tree, invert the tree, and return its root.
# Every node's left and right children are swapped, at every level.
# ----------------------------

# Approach: Recursion (DFS)
# - Base case: an empty tree (root is None) has nothing to invert
# - Recursively invert the left and right subtrees
# - Swap them onto root: root.left = inverted right, root.right = inverted left
# Time: O(n) — visits every node in the tree exactly once 
# Space: O(h) — call stack depth equals tree height, worst case O(n) for a skewed tree.

from typing import Optional

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left 
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None

        new_right = self.invertTree(root.left)
        new_left = self.invertTree(root.left)


        root.left = new_left
        root.right = new_right

        return root

#------------------------
# Test cases
#------------------------

if __name__ == "__main__":
    sol = Solution()

    # Tree: [4,2,7,1,3,6,9] -> inverted: [4,7,2,9,6,3,1]
    root1 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    result1 = sol.invertTree(root1)
    print(result1.val, result1.left.val, result1.right.val) # expected: 2 3 1

    # Tree: [2,1,3] -> inverted: [2,3,1]
    root2 = TreeNode(2, TreeNode(1), TreeNode(3))
    result2 = sol.invertTree(root2)
    print(result2.val, result2.left.val, result2.right.val)  # expected: 2 3 1

    # Empty tree
    print(sol.invertTree(None))  # expected: None