# 1971. Find if Path Exists in Graph
# Difficulty: Easy
# Topic: Graph, BFS, Union Find
# Link: https://leetcode.com/problems/find-if-path-exists-in-graph/

# ----------------------------
# Problem:
# Given n vertices and a list of undirected edges, plus a source and
# destination vertex, return True if there is a valid path from source
# to destination, False otherwise.
# ----------------------------

# Approach: Build adjacency list, then BFS
# - Build an adjacency list from the flat edges list (undirected, so
#   each edge is added both ways)
# - Run standard BFS from source, tracking visited vertices
# - If destination is ever reached during BFS, return True
# - If BFS finishes without reaching destination, return False
# Time: O(V + E) — visits every vertex and edge at most once | Space: O(V + E) — adjacency list plus the visited set and queue

from collections import deque
from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = {i: [] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        queue = deque([source])
        visited.add(source)

        while queue:
            current = queue.popleft()
            if current == destination:
                return True
            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return False

# ----------------------------
# Test cases
# ----------------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.validPath(3, [[0,1],[1,2],[2,0]], 0, 2))  # expected: True
    print(sol.validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5))  # expected: False