# 200. Number of Islands
# Difficulty: Medium
# Topic: BFS, DFS, Graph, Matrix
# Link: https://leetcode.com/problems/number-of-islands/

# ----------------------------
# Problem:
# Given an m x n 2D binary grid 'grid' which represents a map of '1's
# (land) and '0's (water), return the number of islands. An island is
# surrounded by water and is formed by connecting adjacent lands
# horizontally or vertically. You may assume all four edges of the
# grid are all surrounded by water.
# ----------------------------

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0

        # Approach: DFS flood-fill
        # - Scan every cell; whenever unvisited land ('1') is found,
        #   that's a new island, so increment the count
        # - "Sink" that entire connected island (turn '1's to '0') so
        #   we never count the same island twice
        # - Time: O(rows * cols) — every cell is visited at most twice
        # - Space: O(rows * cols) — worst case recursion depth if the
        #   whole grid is one giant island
        def sink(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
                return
            grid[r][c] = "0"
            sink(r + 1, c)
            sink(r - 1, c)
            sink(r, c + 1)
            sink(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    sink(r, c)

        return islands


# ----------------------------
# Test cases
# ----------------------------
if __name__ == "__main__":
    sol = Solution()

    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    print(f"Islands: {sol.numIslands(grid1)}")  # Expected: 1

    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    print(f"Islands: {sol.numIslands(grid2)}")  # Expected: 3