# 206. Reverse Linked List
# Difficulty: Easy
# Topic: Linked List
# Link: https://leetcode.com/problems/reverse-linked-list/

# ----------------------------
# Problem:
# Given the head of a singly linked list, reverse the list,
# and return the reversed list.
# ----------------------------

# Approach: Iterative pointer reversal
# - Walk through the list once
# - At each node, flip its .next to point backward instead of forward
# - Save the forward node before overwriting it, or you lose the rest of the list
# Time: O(n) | Space: O(1)

from typing import Optional

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val= val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode])  -> Optional[ListNode]:
        prev = None 
        current = head

        while current is not None:
            next_node = current.next
            current.next = prev 
            prev = current
            current = next_node

        return prev

    # ------------------------------
    # Test cases
    # ------------------------------

def build_list(values):
    dummy = ListNode()
    current = dummy 
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next

def list_to_array(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

if __name__ == "__main__":
    sol = Solution()

    head1 = build_list([1, 2, 3, 4, 5])
    print(list_to_array (sol.reverseList(head1))) # expected: [5, 4, 3, 2,1]

    head2 = build_list([1, 2])
    print(list_to_array(sol.reverseList(head2))) # expected: [2, 1]

    head3 = build_list([])
    print(list_to_array(sol.reverseLIst(head3))) # expected[]

    

