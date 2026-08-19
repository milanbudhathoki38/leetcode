# 141. Linked List Cycle
# Difficulty: Easy
# Topic: Linked List
# Link: https://leetcode.com/problems/linked-list-cycle/

# ----------------------------
# Problem:
# Given head, the head of a linked list, determine if the linked
# list has a cycle in it.
# ----------------------------

# Approach: Floyd's Cycle Detection (fast/slow pointers)
# - slow moves 1 step per iteration, fast moves 2 steps
# - if there's no cycle, fast reaches the end (None) first
# - if there IS a cycle, fast eventually catches up to slow —
#   since fast closes the gap by 1 extra step every iteration
# Time: O(n) | Space: O(1)

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

# ----------------------------
# Test cases
# ----------------------------
def build_list_with_cycle(values, pos):
    # pos = index the tail connects back to, or -1 for no cycle
    if not values:
        return None
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0]

if __name__ == "__main__":
    sol = Solution()

    head1 = build_list_with_cycle([3, 2, 0, -4], 1)
    print(sol.hasCycle(head1))  # expected: True

    head2 = build_list_with_cycle([1, 2], -1)
    print(sol.hasCycle(head2))  # expected: False

    head3 = build_list_with_cycle([1], -1)
    print(sol.hasCycle(head3))  # expected: False