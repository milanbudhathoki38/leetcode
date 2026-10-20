# 1584. Min Cost to Connect All Points
# Difficulty: Medium
# Topic: Array, Union Find, Graph, Minimum Spanning Tree
# Link: https://leetcode.com/problems/min-cost-to-connect-all-points/

# ----------------------------
# Problem:
# You are given an array of points on a 2D plane, where points[i] is
# [xi, yi]. The cost of connecting two points is the Manhattan distance
# between them: |xi - xj| + |yi - yj|. Return the minimum cost to make
# all points connected, where there is exactly one simple path between
# any two points.
# ----------------------------

# Approach: Kruskal's Algorithm with Union Find
# - Build every possible edge between two points, stored as (cost, i, j)
# - Sort the edges so the cheapest ones come first
# - Start with every point as its own group, parent[i] = i
# - Go through the sorted edges and find the captain of both points
# - If the captains are different, the points are in separate groups,
#   so take the edge: merge the groups and add the cost to the total
# - If the captains are the same, they are already connected, so skip it
# - The edges taken form the minimum spanning tree, and total is its cost
# Time: O(n^2 log n) — about n^2 edges get built and sorted | Space: O(n^2) — the list of all edges

from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []

        for i in range(n):
            for j in range(i + 1, n):
                cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((cost, i, j))

        edges.sort()

        parent = list(range(n))

        def find(x: int) -> int:
            if parent[x] == x:
                return x
            return find(parent[x])

        total = 0

        for cost, i, j in edges:
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_j] = root_i
                total += cost

        return total


# ----------------------------
# Test cases
# ----------------------------
if __name__ == "__main__":
    sol = Solution()
    print(f"Test 1: {sol.minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]])}")  # Expected: 20
    print(f"Test 2: {sol.minCostConnectPoints([[3, 12], [-2, 5], [-4, 1]])}")  # Expected: 18
    print(f"Test 3: {sol.minCostConnectPoints([[0, 0]])}")  # Expected: 0
