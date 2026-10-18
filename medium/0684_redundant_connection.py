# 684. Redundant Connection
# Difficulty: Medium
# Topic: Graph, Union Find, Disjoint Set
# Link: https://leetcode.com/problems/redundant-connection/

# ----------------------------
# Problem:
# A tree with n nodes (labeled 1 to n) had one extra edge added. Given
# the list of edges, return the edge that can be removed so the graph
# is a tree again. If there are several answers, return the one that
# appears last in the input.
# ----------------------------

# Approach: Union Find (Disjoint Set)
# - Start with every node as its own group, parent[i] = i
# - find(x) walks up the parent links until it reaches the group captain
# - For each edge, find the captain of both ends
# - If the captains match, the nodes are already connected, so this edge
#   closes a cycle and is the answer
# - If not, merge the groups by making one captain the boss of the other
# Time: O(n^2) worst case — find can walk a long chain (path compression would make it near O(n)) | Space: O(n) — the parent list

from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))

        def find(x: int) -> int:
            if parent[x] == x:
                return x
            return find(parent[x])

        for a, b in edges:
            root_a = find(a)
            root_b = find(b)
            if root_a == root_b:
                return [a, b]
            parent[root_b] = root_a

        return []


# ----------------------------
# Test cases
# ----------------------------
if __name__ == "__main__":
    sol = Solution()
    print(f"Test 1: {sol.findRedundantConnection([[1, 2], [1, 3], [2, 3]])}")  # Expected: [2, 3]
    print(f"Test 2: {sol.findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]])}")  # Expected: [1, 4]
