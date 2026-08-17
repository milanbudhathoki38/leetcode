# 21. Merge Two Sorted Lists
# Difficulty: Easy
# Topic: Linked List
# Link: https://leetcode.com/problems/merge-two-sorted-lists/

# ----------------------------
# Problem:
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list by splicing together the
# nodes of the two lists. Return the head of the merged linked list.
# ----------------------------

# Approach: Two-pointer merge
# - Walk list1 and list2 at the same time, comparing one value at a time
# - Whichever node has the smaller value gets attached next, and only
#   that list's pointer moves forward
# - On a tie, list1 wins (since the comparison uses <=)
# - Once one list runs out, attach whatever's left of the other list directly —
#   it's already sorted, no more comparisons needed
# - A dummy node is used so there's always something to attach the first
#   real node to, avoiding a special case for "is this the first node"
# Time: O(n + m) | Space: O(1)

from typing import Optional

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        tail.next = list1 if list1 else list2

        return dummy.next
    
# ----------------------------
# Test cases 
# ----------------------------

def build_list(values):
    dummy = ListNode()
    current = dummy 
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next

def list_to_array(node):
    result =[]
    while node:
        result.append(node.val)
        node = node.next
    return result 

if __name__ == "__main__":
    sol = Solution()

    l1 = build_list([1, 2, 4])
    l2 = build_list([1, 3, 4])
    print(list_to_array(sol.mergeTwoLists(l1, l2))) # [1, 1, 2, 3, 4, 4]

    l3 = build_list([])
    l4 = build_list([])
    print(list_to_array(sol.mergeTwoLists(l3, l4))) # []

    l5 = build_list([])
    l6 = build_list([0])
    print(list_to_array(sol.mergeTwoLists(l5, l6))) # [0]

    l7 = build_list([1, 4, 8])
    l8 = build_list([2, 5, 9])
    print(list_to_array(sol.mergeTwoLists(l7, l8))) 
            
        
    
