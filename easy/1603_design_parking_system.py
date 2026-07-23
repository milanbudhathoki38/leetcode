# 1603. Design Parking System
# Difficulty: Easy
# Topic: OOP Design, Simulation
# Link: https://leetcode.com/problems/design-parking-system/

# ----------------------------
# Problem:
# Design a parking system for a lot with 3 sizes: big, medium, small,
# each with fixed capacity. Implement addCar(carType) which returns
# True if a car of that type can park (there's still room), decrementing
# that size's remaining capacity. Returns False if no room is left.
# ----------------------------

# Approach: Instance Variables as Remaining Capacity Counters
# - store each size's remaining spot count as an instance variable
# - branch on carType (1=big, 2=medium, 3=small) to check the right counter
# - if capacity > 0: decrement it and return True
# - otherwise: return False
# Time: O(1) per addCar call | Space: O(1)


class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.big > 0:
                self.big -= 1
                return True
            else:
                return False
        elif carType == 2:
            if self.medium > 0:
                self.medium -= 1
                return True
            else:
                return False
        elif carType == 3:
            if self.small > 0:
                self.small -= 1
                return True
            else:
                return False


# ----------------------------
# Test cases
# ----------------------------
if __name__ == "__main__":
    obj = ParkingSystem(1, 1, 0)
    print(f"addCar(1) = {obj.addCar(1)}")  # True
    print(f"addCar(2) = {obj.addCar(2)}")  # True
    print(f"addCar(3) = {obj.addCar(3)}")  # False (no small spots)
    print(f"addCar(1) = {obj.addCar(1)}")  # False (big spot already taken)