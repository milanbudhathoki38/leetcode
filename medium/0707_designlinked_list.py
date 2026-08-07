# 707. Design Linked List
# Difficulty: Medium
# Topic: Linked List, OOP Design
# Link: https://leetcode.com/problems/design-linked-list/

# ----------------------------
# Problem:
# Design a singly linked list, supporting get(index), addAtHead(val),
# addAtTail(val), addAtIndex(index, val), and deleteAtIndex(index).
# ----------------------------

# Approach: Node Chain with Head Pointer + Size Tracking
# - each Node holds a value and a reference to the next Node (or None)
# - MyLinkedList tracks self.head (first node, or None if empty) and
#   self.size (current length, avoids re-counting every operation)
# - get/addAtIndex/deleteAtIndex all walk forward from head, counting steps
# - addAtHead/addAtTail are O(1) and O(n) respectively; addAtIndex reuses
#   both as shortcuts for the head/tail edge cases
# - insertion/deletion always requires rewiring .next pointers in the
#   correct order to avoid losing the rest of the chain
# Time: get/addAtIndex/deleteAtIndex O(n), addAtHead O(1), addAtTail O(n)
# Space: O(n) for the list itself, O(1) per operation


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        current = self.head
        for _ in range(index):
            current = current.next

        return current.val

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return

        if index <= 0:
            self.addAtHead(val)
            return

        if index == self.size:
            self.addAtTail(val)
            return

        new_node = Node(val)
        current = self.head
        for _ in range(index - 1):
            current = current.next

        new_node.next = current.next
        current.next = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return

        current = self.head
        for _ in range(index - 1):
            current = current.next

        current.next = current.next.next
        self.size -= 1


# ----------------------------
# Test cases
# ----------------------------
if __name__ == "__main__":
    obj = MyLinkedList()
    obj.addAtHead(1)
    obj.addAtTail(3)
    obj.addAtIndex(1, 2)
    print(f"get(1) = {obj.get(1)}")  # 2

    obj.deleteAtIndex(1)
    print(f"get(1) = {obj.get(1)}")  # 3

    obj2 = MyLinkedList()
    obj2.addAtHead(7)
    obj2.addAtHead(3)
    print(f"get(0) = {obj2.get(0)}")  # 3
    print(f"get(1) = {obj2.get(1)}")  # 7
    print(f"get(2) = {obj2.get(2)}")  # -1 (out of bounds)

    # empty list edge cases 

    obj3 = MyLinkedList()
    print(f"get(0) on empty list = {obj3.get(0)}") # -1
    obj3.deleteAtIndex(0) # should do nothing,  no crash 
    print(f"size after deleting from empty list = {obj3.size}") # 0

    #addAtIndex with index == size (should behave like addAtTail)

    obj4 = MyLinkedList()
    obj4.addAtHead(10)
    obj4.addAtHead(20)
    obj4.addAtIndex(2, 30) # index == size, append at tail 
    print(f"get(2) after addAtIndex(2, 30) = {obj4.get(2)}") # 30

    # addAtIndex with negative index (should behave like addAtHead)

    obj5 = MyLinkedList()
    obj5.addAtTail(100)
    obj5.addAtIndex(-5, 200)
    print(f"get(0) after addAtIndex(-5, 200)= {obj5.get(0)}") # 200

    # addAtIndex with index > size (should do nothing)
    obj6 = MyLinkedList()
    obj6.addAtHead(1)
    obj6.addAtIndex(10, 999) # invalid, size is only 1
    print(f"size after invalid addAtIndex = {obj6.size}") # 1

    # deleting the only node in the list 
    obj7 = MyLinkedList()
    obj7.addAtHead(5)
    obj7.deleteAtIndex(0)
    print(f"size after deleting only node = {obj7.size}") # 0
    print(f"get(0) after deleting only node = {obj7.get(0)}") # -1

    # chain of adds and deltes together 
    obj8 = MyLinkedList()
    obj8.addAtTail(1)
    obj8.addAtTail(2)
    obj8.addAtTail(3)
    obj8.deleteAtIndex(1)
    obj8.addAtIndex(1, 99)
    print(f"final list values: {obj8.get(0)}, {obj8.get(1)}, {obj8.get(2)}")

