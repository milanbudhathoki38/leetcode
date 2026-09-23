# 1791. Find Center of Star Graph
# Difficulty: Easy
# Topic: Arrays, Graphs
# Link: https://leetcode.com/problems/find-center-of-star-graph/

# ----------------------------
# Problem:
# Given the edges of a valid star graph, return the center vertex.
# The center is the vertex connected to every other vertex.
# ----------------------------

# Approach: Compare the First Two Edges
# - the center vertex must appear in every edge
# - examine the first two edges
# - check each vertex in the first edge
# - return the vertex that also appears in the second edge
# Time: O(1) | Space: O(1)

from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        first_edge = edges[0]
        second_edge = edges[1]

        for vertex in first_edge:
            if vertex in second_edge:
                return vertex

        return -1


# ----------------------------
# Test cases
# ----------------------------
if __name__ == "__main__":
    sol = Solution()

    edges = [[1, 2], [2, 3], [4, 2]]
    print(f"center = {sol.findCenter(edges)}")  # center = 2

    edges = [[1, 2], [5, 1], [1, 3], [1, 4]]
    print(f"center = {sol.findCenter(edges)}")  # center = 1

    edges = [[10, 7], [3, 7], [7, 4], [5, 7]]
    print(f"center = {sol.findCenter(edges)}")  # center = 7