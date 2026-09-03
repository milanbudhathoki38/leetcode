# 700. Search in a Binary Search Tree
# Difficulty: Easy
# Topic: Tree, Binary Search Tree, Binary Tree
# Link: https://leetcode.com/problems/search-in-a-binary-search-tree/

# ----------------------------
# Problem:
# Given the root of a binary search tree and an integer val, find the
# node in the BST whose value equals val, and return the subtree rooted
# at that node. If no such node exists, return None.
# ----------------------------

# Approach: Iterative walk using BST ordering
# - Start at root, compare val against the current node's value
# - If equal, found it, return the node
# - If val is smaller, move left; if bigger, move right
# - If we walk off the tree (hit None), the value doesn't exist
# Time: O(h) — h is tree height, worst case O(n) for a skewed tree, O(log n) for a balanced tree | Space: O(1) — iterative, no recursion, no extra memory used

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root is not None:
            if val == root.val:
                return root
            elif val < root.val:
                root = root.left
            else:
                root = root.right
        return None

# ----------------------------
# Test cases
# ----------------------------
if __name__ == "__main__":
    sol = Solution()

    # Tree: [4,2,7,1,3] -> search 2 -> return subtree rooted at 2: [2,1,3]
    root1 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
    result1 = sol.searchBST(root1, 2)
    print(result1.val if result1 else None)  # expected: 2

    # Tree: [4,2,7,1,3] -> search 5 -> not found
    result2 = sol.searchBST(root1, 5)
    print(result2)  # expected: None