# 705. Design HashSet
# Difficulty: Easy
# Topic: OOP Design, Hash Set
# Link: https://leetcode.com/problems/design-hashset/

# ----------------------------
# Problem:
# Design a HashSet without using any built-in hash table libraries.
# Implement MyHashSet with add(key), remove(key), and contains(key),
# supporting insertion, deletion, and membership checking.
# ----------------------------

# Approach: OOP Wrapper Around a Set
# - store all inserted keys in self.data, a Python set
# - add(key): insert directly, sets naturally ignore duplicates
# - remove(key): check membership first to avoid a KeyError, then remove
# - contains(key): return the boolean result of Python's "in" operator directly
# Note: this uses Python's built-in set for the underlying storage.
# A from-scratch version (array + custom hash function + collision
# handling) is a natural follow-up once hashing internals are covered.
# Time: O(1) average per operation | Space: O(n)


class MyHashSet:

    def __init__(self):
        self.data = set()

    def add(self, key: int) -> None:
        self.data.add(key)

    def remove(self, key: int) -> None:
        if key in self.data:
            self.data.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.data


# ----------------------------
# Test cases
# ----------------------------
if __name__ == "__main__":
    obj = MyHashSet()
    print(f"add(1) = {obj.add(1)}")            # None
    print(f"add(2) = {obj.add(2)}")             # None
    print(f"contains(1) = {obj.contains(1)}")   # True
    print(f"contains(3) = {obj.contains(3)}")   # False
    print(f"add(2) = {obj.add(2)}")             # None (duplicate, no effect)
    print(f"contains(2) = {obj.contains(2)}")   # True
    print(f"remove(2) = {obj.remove(2)}")        # None
    print(f"contains(2) = {obj.contains(2)}")   # False