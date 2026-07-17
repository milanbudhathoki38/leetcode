# 1732. Find the Highest Altitude
# Difficulty: Easy
# Topic: Array, Prefix Sum
# Link: https://leetcode.com/problems/find-the-highest-altitude/

# ----------------------------
# Problem:
# A biker starts at altitude 0. Given gain, where gain[i] is the
# net altitude change between point i and i+1, return the highest
# altitude reached at any point during the trip.
# ----------------------------

# Approach: Running Total with Max Tracking
# - keep a running current_altitude by adding each gain value
# - track the highest current_altitude ever seen
# - starting altitude of 0 counts as a candidate too
# Time: O(n) | Space: O(1)

from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_altitude = 0
        highest = 0
        for change in gain:
            current_altitude += change
            if current_altitude > highest:
                highest = current_altitude
        return highest


# ----------------------------
# Test cases
# ----------------------------
if __name__ == "__main__":
    sol = Solution()

    gain = [-5, 1, 5, 0, -7]
    print(f"largestAltitude = {sol.largestAltitude(gain)}")  # 1

    gain = [-4, -3, -2, -1, 4, 3, 2]
    print(f"largestAltitude = {sol.largestAltitude(gain)}")  # 0