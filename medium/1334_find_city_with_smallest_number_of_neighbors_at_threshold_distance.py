# 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance
# Difficulty: Medium
# Topic: Graph, Shortest Path, Floyd-Warshall
# Link: https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

#--------------------------
# Problem:
# There are n cities connected by weighted undirected edges.
# Each edge is represented as [src, dst, weight].
# Find the city with the smallest number of cities that can be reached
# within distanceThreshold using the shortest possible path.
# If there is a tie, return the city with the greatest number.
#--------------------------

# Approach: Floyd-Warshall
# - Build a distance matrix where dist[i][j] stores the shortest distance
#   between city i and city j.
# - Start with infinity for cities that are not directly connected.
# - Set the distance from each city to itself to 0.
# - Store each direct edge's weight in the matrix.
# - Use Floyd-Warshall to find the shortest path between every pair of cities.
# - Count how many cities each city can reach within distanceThreshold.
# - If there is a tie, choose the city with the greater number.
# Time: O(n^3) | Space: O(n^2)

class Solution:
    def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:

        # Create distance matrix
        dist = [[float("inf")] * n for _ in range(n)]

        # Distance from a city to itself is 0
        for i in range(n):
            dist[i][i] = 0

        # Add the edges
        for src, dst, weight in edges:
            dist[src][dst] = weight
            dist[dst][src] = weight

        # Find shortest distances between every pair of cities
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(
                        dist[i][j],
                        dist[i][k] + dist[k][j]
                    )

        # Find city with the fewest reachable cities
        # If tied, choose the city with the larger number
        best_city = -1
        min_count = float("inf")

        for i in range(n):
            count = 0

            for j in range(n):
                if i != j and dist[i][j] <= distanceThreshold:
                    count += 1

            if count <= min_count:
                min_count = count
                best_city = i

        return best_city