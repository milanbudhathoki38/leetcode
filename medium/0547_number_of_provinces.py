# 547. Number of Provinces
# Difficulty: Medium
# Topic: Graphs, Depth-First Search, Adjacency Matrix
# Link: https://leetcode.com/problems/number-of-provinces/

# ----------------------------
# Problem:
# Given an adjacency matrix representing connections between cities,
# return the total number of provinces.
#
# A province is a group of directly or indirectly connected cities.
# A city by itself also counts as one province.
# ----------------------------

# Approach: DFS Connected Components
# - loop through every city
# - if a city has not been visited, it begins a new province
# - increase the province count and run DFS from that city
# - DFS visits every city connected to the current province
# - use matrix[city][neighbor] to check whether two cities are connected
# Time: O(n^2) | Space: O(n)

from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        provinces = 0

        def dfs(city: int) -> None:
            visited.add(city)

            for neighbor in range(n):
                if (
                    isConnected[city][neighbor] == 1
                    and neighbor not in visited
                ):
                    dfs(neighbor)

        for city in range(n):
            if city not in visited:
                provinces += 1
                dfs(city)

        return provinces


# ----------------------------
# Test cases
# ----------------------------
if __name__ == "__main__":
    sol = Solution()

    connections = [
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 1]
    ]
    print(f"provinces = {sol.findCircleNum(connections)}")  # provinces = 2

    connections = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]
    print(f"provinces = {sol.findCircleNum(connections)}")  # provinces = 3

    connections = [
        [1, 1, 0],
        [1, 1, 1],
        [0, 1, 1]
    ]
    print(f"provinces = {sol.findCircleNum(connections)}")  # provinces = 1