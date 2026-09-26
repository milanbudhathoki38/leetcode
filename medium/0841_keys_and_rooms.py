# 841. Keys and Rooms
# Difficulty: Medium
# Topic: Graphs, Depth-First Search
# Link: https://leetcode.com/problems/keys-and-rooms/

# ----------------------------
# Problem:
# There are n rooms, and room 0 is initially unlocked.
# Each room contains keys that can unlock other rooms.
# Return True if every room can be visited and False otherwise.
# ----------------------------

# Approach: Depth-First Search
# - start DFS from room 0 because it is initially unlocked
# - add every entered room to the visited set
# - each key represents another room that can be visited
# - recursively visit every unvisited room for which we find a key
# - compare the number of visited rooms with the total number of rooms
# Time: O(V + E) | Space: O(V)

from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited: set[int] = set()

        def dfs(room: int) -> None:
            visited.add(room)

            for key in rooms[room]:
                if key not in visited:
                    dfs(key)

        dfs(0)

        return len(visited) == len(rooms)


# ----------------------------
# Test cases
# ----------------------------
if __name__ == "__main__":
    sol = Solution()

    rooms = [[1], [2], [3], []]
    print(f"can_visit_all = {sol.canVisitAllRooms(rooms)}")
    # can_visit_all = True

    rooms = [[1, 3], [3, 0, 1], [2], [0]]
    print(f"can_visit_all = {sol.canVisitAllRooms(rooms)}")
    # can_visit_all = False

    rooms = [[]]
    print(f"can_visit_all = {sol.canVisitAllRooms(rooms)}")
    # can_visit_all = True