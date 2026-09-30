# 743. Network Delay Time
# Difficulty: Medium
# Topic: Graph, Dijkstra, Heap
# Link: https://leetcode.com/problems/network-delay-time/

# --------------------------
# Problem:
# Given directed edges [start, end, cost], find the time needed
# for a signal starting at node k to reach all n nodes.
# Return -1 if any node cannot be reached.
# --------------------------

# Approach: Dijkstra's Algorithm
# - Build an adjacency list of neighbors and edge costs.
# - Use a min-heap to process the smallest total distance first.
# - Update a neighbor when a shorter route is found.
# - Return the largest shortest distance among all nodes.
# Time: O((V + E) log(E + 1)) | Space: O(V + E)

import heapq
from collections import defaultdict
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for start, end, cost in times:
            graph[start].append((end, cost))

        distances = [float("inf")] * (n + 1)
        distances[k] = 0
        heap = [(0, k)]

        while heap:
            current_distance, node = heapq.heappop(heap)

            if current_distance > distances[node]:
                continue

            for neighbor, cost in graph[node]:
                new_distance = current_distance + cost

                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(heap, (new_distance, neighbor))

        answer = max(distances[1:])

        if answer == float("inf"):
            return -1

        return answer


# --------------------------
# Test cases
# --------------------------

if __name__ == "__main__":
    sol = Solution()

    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    print(sol.networkDelayTime(times, 4, 2))  # 2

    times = [[1, 2, 1]]
    print(sol.networkDelayTime(times, 2, 1))  # 1

    times = [[1, 2, 1]]
    print(sol.networkDelayTime(times, 2, 2))  # -1

    times = [[1, 2, 6], [1, 3, 2], [3, 2, 1]]
    print(sol.networkDelayTime(times, 3, 1))  # 3

    times = []
    print(sol.networkDelayTime(times, 1, 1))  # 0